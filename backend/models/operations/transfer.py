from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .operation import Operation


# Classe de transferência
class Transfer(Operation):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(
        ForeignKey("operations.id"),
        primary_key=True
    )

    account_from_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=False
    )

    account_to_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=False
    )

    __mapper_args__ = {
        "polymorphic_identity": "transfer"
    }