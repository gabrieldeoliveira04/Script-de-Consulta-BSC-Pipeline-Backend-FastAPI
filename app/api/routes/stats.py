from fastapi import APIRouter
from sqlalchemy import func

from app.database.session import SessionLocal
from app.models.balance import Balance


router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)


@router.get(

    "",

    summary="Get monitoring statistics",

    description="""
Returns monitoring statistics.

Includes:

- total records stored
- wallet with highest balance
"""
)

def get_stats():

    db = SessionLocal()

    try:

        total_records = (

            db.query(
                Balance
            ).count()

        )

        highest_balance = (

            db.query(Balance)

            .order_by(
                Balance.balance.desc()
            )

            .first()

        )

        return {

            "total_records":
            total_records,

            "wallet_with_highest_balance": {

                "wallet":
                highest_balance.wallet_address,

                "balance":
                highest_balance.balance

            }

        }

    finally:

        db.close()