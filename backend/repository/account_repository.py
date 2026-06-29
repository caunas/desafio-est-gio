from sqlalchemy import select

from models import Account, CheckingAccount, SavingsAccount



class AccountRepository:
    # Recebe a sessão do database no construtor
    def __init__(self, db):
        self.db = db

    def getAllAccounts(self):
        checking = self.db.scalars(select(CheckingAccount)).all()
        savings = self.db.scalars(select(SavingsAccount)).all()

        return checking + savings
    
    def getById(self, account_id: int):
        account = self.db.get(CheckingAccount, account_id)

        if account is None:
            account = self.db.get(SavingsAccount, account_id)

        return account

    def save(self, account: Account):
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def update(self):
        self.db.commit()
        self.db.refresh()
        return account

    def delete(self, account: Account):
        self.db.delete(account)
        self.db.commit()
