from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Operation


class OperationRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, operation: Operation) -> Operation:
        self.db.add(operation)
        self.db.commit()
        self.db.refresh(operation)
        return operation

    def get_by_id(self, operation_id: int) -> Operation | None:
        return self.db.get(Operation, operation_id)

    def get_all(self) -> list[Operation]:
        return self.db.scalars(
            select(Operation)
        ).all()

    def get_by_type(self, operation_type: str) -> list[Operation]:
        return self.db.scalars(
            select(Operation).where(Operation.operation_type == operation_type)
        ).all()


    def delete(self, operation: Operation) -> None:
        self.db.delete(operation)
        self.db.commit()