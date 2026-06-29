from models.account import Account


class AccountRepository:
    # Recebe a sessão do database no construtor
    def __init__(self, db):
        self.db = db
    
    def getById(self, account_id, int):
        return self.db.get(Account, account_id)

    def save(self, account: Account):
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def update(self):
        self.db.commit()
        self.db.refresh()
        return account

    def delete(self):
        db.delete(account)
        db.commit()
