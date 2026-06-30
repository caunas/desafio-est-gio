from enum import Enum


class OperationType(str, Enum):
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"
    TRANSFER = "transfer"