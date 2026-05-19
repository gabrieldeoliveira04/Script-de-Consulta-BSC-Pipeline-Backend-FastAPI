from fastapi import FastAPI

from app.api.routes.balances import (
    router as balance_router
)
from app.api.routes.stats import (
    router as stats_router
)



app = FastAPI(
    title="BSC Balance Monitor API",
    version="1.0.0"
)

app.include_router(
    stats_router
)


app.include_router(
    balance_router
)

app.include_router(
    stats_router
)


@app.get("/")
def health_check():

    return {
        "status": "online"
    }