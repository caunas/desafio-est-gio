from fastapi import APIRouter, Depends

from models import CheckingAccount
from models import SavingsAccount
from service.account_service import *
from schemas.account_schema import CheckingAccountCreate, SavingsAccountCreate, AccountResponse
from repository.account_repository import AccountRepository
from core.db import get_db

router = APIRouter(
    prefix="/account",
    tags=["Account"]
)

# Injetar dependências dessa forma escala melhor
def get_account_service(db = Depends(get_db)) -> AccountService:
    return AccountService(db)


@router.post("/checking", 
response_model = AccountResponse, 
status_code = 201)
def create_checking_account(
    data: CheckingAccountCreate,
    db = Depends(get_db),
    service: AccountService = Depends(get_account_service)
):

    return service.create_checking_account(
        holder_name=data.holder_name,
        initial_balance=data.initial_balance,
    )

@router.post("/saving",
response_model = AccountResponse,
status_code = 201)
def create_saving_account(
    data: SavingsAccountCreate,
    db = Depends(get_db),
    service: AccountService = Depends(get_account_service)
):
    return service.create_savings_account(
        holder_name = data.holder_name,
        initial_balance = data.initial_balance
    )

@router.get("/all",
response_model = list[AccountResponse],
status_code = 200)
def get_all_accounts(
    db = Depends(get_db),
    service: AccountService = Depends(get_account_service)
):
    return service.get_all_accounts()

@router.delete("/accounts/{id}",
response_model = AccountResponse,
status_code = 200)
def delete_account(
    db = Depends(get_db),
    service: AccountService = Depends(get_account_service),
    id_victim = id
):
    return service.delete_account(id_victim=id_victim)
