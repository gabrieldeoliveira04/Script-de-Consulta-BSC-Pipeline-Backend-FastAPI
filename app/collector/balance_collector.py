from app.database.session import SessionLocal

from app.models.balance import Balance

from app.services.bsc_service import BSCService

from app.config.settings import settings


def collect_balances():

    db = SessionLocal()

    service = BSCService(
        settings.RPC_URL
    )

    try:

        for wallet in settings.WALLETS:

            balance = (
                service.get_token_balance(
                    wallet,
                    settings.TOKEN_ADDRESS
                )
            )
            # teste temporário 
            balance *= 1.10

            balance_record = Balance(

                wallet_address=wallet,

                token_address=settings.TOKEN_ADDRESS,

                balance=float(balance)

            )

            db.add(
                balance_record
            )

        db.commit()

        print(
            "Balances saved successfully"
        )

    except Exception as error:

        db.rollback()

        print(
            f"Collection failed: {error}"
        )

    finally:

        db.close()