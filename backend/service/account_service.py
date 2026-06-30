from repository.account_repository import AccountRepository
from repository.operation_repository import OperationRepository

from decimal import Decimal
from fastapi import HTTPException 

from models import Account, CheckingAccount, SavingsAccount
from models import Deposit, Withdraw, Transfer


class AccountService:
    
    def __init__(self, db, repository: AccountRepository | None = None, operation_repository: OperationRepository | None = None):
        self.repository = repository or AccountRepository(db)
        self.operationRepository = operation_repository or OperationRepository(db)
        print("SERVICE INIT DB TYPE:", type(db))

    def create_checking_account(
        self, 
        holder_name: str, 
        initial_balance: Decimal = Decimal("0.00")
    ) -> CheckingAccount:

        account = CheckingAccount(
            holder_name = holder_name,
            balance = initial_balance
        )

        return self.repository.save(account)

    def create_savings_account(
        self,
        holder_name: str,
        initial_balance: Decimal = Decimal("0.00")
    ) -> SavingsAccount:
        
        account = SavingsAccount(
            holder_name = holder_name,
            balance = initial_balance
        )

        return self.repository.save(account)

    def get_all_accounts(self):
        return self.repository.getAllAccounts()

    def delete_account(
        self,
        id_victim: int):
        victim = self.repository.getById(id_victim)

        if victim is None:
            raise HTTPException(status_code = 404, detail="Conta não encontrada.")
        
        self.repository.delete(victim)
        return victim

    def deposit(self, account_id: int, amount: Decimal):
        account = self.repository.getById(account_id)

        if account is None:
            raise HTTPException(status_code = 404, detail="Conta não encontrada.")

        account.balance += amount

        operation = Deposit(
            amount=amount,
            account_id=account.id
        )

        self.operationRepository.save(operation)
        return self.repository.save(account)

    def withdraw(self, account_id: int, amount: Decimal):
        account = self.repository.getById(account_id)

        if account is None:
            raise HTTPException(status_code = 404, detail="Conta não encontrada.")

        final_amount = amount

        if isinstance(account, CheckingAccount):
            final_amount += account.tax

        new_balance = account.balance - final_amount

        if isinstance(account, SavingsAccount) and new_balance < 0:
            raise HTTPException(status_code = 400, detail="Conta poupança não pode ficar negativa.")

        account.balance = new_balance

        operation = Withdraw(
            amount=amount,
            account_from_id=account.id,
            account_to_id=None
        )

        self.operationRepository.save(operation)
        return self.repository.save(account)

    def transfer(self, from_id: int, to_id: int, amount: Decimal):
        from_account = self.repository.getById(from_id)
        to_account = self.repository.getById(to_id)

        if from_account is None or to_account is None:
            raise HTTPException(status_code = 404, detail="Conta não encontrada.")

        final_amount = amount

        if isinstance(from_account, CheckingAccount):
            final_amount += from_account.tax

        new_balance = from_account.balance - final_amount

        if isinstance(from_account, SavingsAccount) and new_balance < 0:
            raise HTTPException(status_code = 400, detail="Conta poupança não pode ficar negativa.")

        from_account.balance = new_balance
        to_account.balance += amount

        operation = Transfer(
            amount=amount,
            account_from_id=from_account.id,
            account_to_id=to_account.id
        )

        self.operationRepository.save(operation)

        self.repository.save(from_account)
        self.repository.save(to_account)

        return {
            "from": from_account,
            "to": to_account
        }