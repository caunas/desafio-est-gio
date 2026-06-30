from fastapi import APIRouter, Depends
from decimal import Decimal

from service.account_service import *

from core.db import get_db

router = APIRouter(
    prefix="/operations", 
    tags=["Operations"])


def get_account_service(db = Depends(get_db)) -> AccountService:
    return AccountService(db)


@router.post("/deposit")
def deposit(
    account_id: int, 
    amount: Decimal,
    db = Depends(get_db),
    service: AccountService = Depends(get_account_service)):
    return service.deposit(account_id, amount)


@router.post("/withdraw")
def withdraw(
    account_id: int, 
    amount: Decimal,
    db = Depends(get_db),
    service: AccountService = Depends(get_account_service)):
    return service.withdraw(account_id, amount)


@router.post("/transfer")
def transfer(
    from_id: int, 
    to_id: int, 
    amount: Decimal,
    db = Depends(get_db),
    service: AccountService = Depends(get_account_service)):
    return service.transfer(from_id, to_id, amount)
