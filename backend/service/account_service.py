from repository.account_repository import AccountRepository

from decimal import Decimal
from fastapi import HTTPException 

from models import CheckingAccount
from models import SavingsAccount

class AccountService:
    
    def __init__(self, repository: AccountRepository | None = None):
        self.repository = repository or AccountRepository()

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
