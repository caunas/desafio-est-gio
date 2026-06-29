from decimal import Decimal

from repository.account_repository import AccountRepository


class AccountService():

    def __init__(self):
        self.repository = AccountRepository()

    def deposit(self, account_id: int, amount: Decimal):
        if amount <= 0:
            raise ValueError("Valor inválido.")

        account = self.repository.getById(account)

        if account is None:
            raise ValueError("Conta não encontrada.")

        account.balance += amount

        return self.repository.update(account)
