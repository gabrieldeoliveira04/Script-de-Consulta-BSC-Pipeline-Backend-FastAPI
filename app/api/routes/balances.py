from fastapi import APIRouter
from sqlalchemy import func
from typing import List
from app.schemas.balance_schema import BalanceResponse

from app.database.session import SessionLocal
from app.models.balance import Balance


router = APIRouter(
    prefix="/balances",
    tags=["Balances"]
)


@router.get(
    "/latest",

    response_model=List[BalanceResponse],

    summary="Get latest balances",

    description="Returns the latest balance snapshot for every monitored wallet."
)

def get_latest_balances():

    db = SessionLocal()

    try:

        subquery = (

            db.query(

                Balance.wallet_address,

                func.max(
                    Balance.collected_at
                ).label("latest")

            )

            .group_by(
                Balance.wallet_address
            )

            .subquery()

        )


        results = (

            db.query(Balance)

            .join(

                subquery,

                (Balance.wallet_address == subquery.c.wallet_address)

                &

                (Balance.collected_at == subquery.c.latest)

            )

            .all()

        )

        return results

    finally:

        db.close()


@router.get(

    "/{wallet}/history",

    response_model=List[BalanceResponse],

    summary="Get wallet history",

    description="Returns all historical records for a wallet ordered by date."

)

def get_wallet_history(
    wallet: str
):

    db = SessionLocal()

    try:

        results = (

            db.query(Balance)

            .filter(

                Balance.wallet_address == wallet

            )

            .order_by(

                Balance.collected_at.desc()

            )

            .all()

        )

        return results

    finally:

        db.close()