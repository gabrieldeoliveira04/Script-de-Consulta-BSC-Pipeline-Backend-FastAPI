from fastapi import FastAPI


app = FastAPI(
    title="BSC Balance Monitor API",
    description="API for monitoring Binance wallets on BSC",
    version="1.0.0"
)


@app.get("/")
def health_check():

    return {
        "status": "online"
    }