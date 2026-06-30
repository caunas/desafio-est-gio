from sqlalchemy import select

from models import Account, CheckingAccount, SavingsAccount


class AccountRepository:
    def __init__(self, db):
        print("REPO INIT DB TYPE:", type(db))
        self.db = db

    def getAllAccounts(self):
        return self.db.scalars(select(Account)).all()
    
    def getById(self, account_id: int):
        return self.db.get(Account, account_id)

    def save(self, account: Account):
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def update(self, account: Account):
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def delete(self, account: Account):
        self.db.delete(account)
        self.db.commit()
