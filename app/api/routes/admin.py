from fastapi import APIRouter

from app.collector.balance_collector import (
    collect_balances
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.post("/collect")
def run_collection():

    collect_balances()

    return {
        "message":"collection executed"
    }