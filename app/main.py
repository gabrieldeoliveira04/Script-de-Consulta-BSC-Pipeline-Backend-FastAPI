from fastapi import FastAPI
from app.database.connection import engine
from app.database.session import Base
from app.models.balance import Balance
from app.models.alert import Alert
from app.api.routes.admin import (
    router as admin_router
)
from app.api.routes.alerts import (
    router as alert_router
)
from app.services.scheduler import (
    start_scheduler
)
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
@app.on_event("startup")
def startup():

    Base.metadata.create_all(
        bind=engine
    )

    start_scheduler()

    print(
        "API started successfully"
    )

app.include_router(
    stats_router
)
app.include_router(
    alert_router
)
app.include_router(
    balance_router
) 

@app.get("/")
def health_check():

    return {
        "status": "online"
    }
app.include_router(
    admin_router
)