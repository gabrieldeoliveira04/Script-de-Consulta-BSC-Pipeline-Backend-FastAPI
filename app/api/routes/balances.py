from fastapi import APIRouter
from sqlalchemy import func

from app.database.session import SessionLocal
from app.models.balance import Balance


router = APIRouter(
    prefix="/balances",
    tags=["Balances"]
)


@router.get("/latest")
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


@router.get("/{wallet}/history")
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