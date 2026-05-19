from fastapi import FastAPI
from app.database.connection import engine
from app.database.session import Base
from app.models.balance import Balance
from app.api.routes.balances import (
    router as balance_router
)
from app.api.routes.stats import (
    router as stats_router
)



app = FastAPI(

    title="BSC Balance Monitor API",

    description="""
API for monitoring Binance public wallets on Binance Smart Chain.

Features:

- collect wallet balances
- store history in PostgreSQL
- expose monitoring endpoints
- provide statistics

Built for technical challenge.
""",

    version="1.0.0",

    contact={
        "name":"Gabriel Oliveira"
    }

)

app.include_router(
    stats_router
)


app.include_router(
    balance_router
)
Base.metadata.create_all(
    bind=engine
)

@app.on_event("startup")
def startup():

    print(
        "API started successfully"
    )

@app.get("/")
def health_check():

    return {
        "status": "online"
    }