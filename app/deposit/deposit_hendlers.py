from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from app.deposit.deposit_models import Deposit
from app.database.database import session
from app.deposit.deposit_service import calculate_deposit
from app.deposit.deposit_schema import DepositCreationSchema, DepositSchema

router = APIRouter(prefix='/deposit', tags=['Deposit Get Info'])


@router.get('/all', response_model=list[DepositSchema])
async def get_all_items(db: Session = Depends(session)):
    deposits = db.execute(select(Deposit)).scalars().all()
    return deposits


@router.get('/{id}', response_model=dict[str, float])
async def get_item(id: int, db: Session = Depends(session)) -> dict[str, float]:
    deposit = db.execute(select(Deposit).where(Deposit.id == id)).scalar_one_or_none()
    if deposit:
        results: dict[str, float] = calculate_deposit(deposit)
    return results


@router.post('/create', response_model=dict[str, float])
async def create_item(body: DepositCreationSchema, db: Session = Depends(session)):
    new_deposit = Deposit(periods=body.periods, amount=body.amount, rate=body.rate)

    db.add(new_deposit)
    db.commit()
    db.refresh(new_deposit)

    results: dict[str, float] = calculate_deposit(DepositSchema(new_deposit))
    return results
