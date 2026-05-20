from app.database.session import SessionLocal

from app.models.balance import Balance
from app.models.alert import Alert

from app.services.bsc_service import (
    BSCService
)

from app.config.settings import (
    settings
)


def collect_balances():

    db = SessionLocal()

    service = BSCService(
        settings.RPC_URL
    )

    try:

        for wallet in settings.WALLETS:

            balance = float(

                service.get_token_balance(

                    wallet,

                    settings.TOKEN_ADDRESS

                )

            )
            # teste temporário 
            balance *= 1.10

            last_balance = (

                db.query(
                    Balance
                )

                .filter(

                    Balance.wallet_address
                    == wallet

                )

                .order_by(

                    Balance.collected_at
                    .desc()

                )

                .first()

            )


            if last_balance:

                variation = abs(

                    (

                        balance
                        -
                        last_balance.balance

                    )

                    /

                    last_balance.balance

                ) * 100


                if variation > 5:

                    alert = Alert(

                        wallet_address=
                        wallet,

                        previous_balance=
                        last_balance.balance,

                        current_balance=
                        balance,

                        variation_percent=
                        variation

                    )

                    db.add(
                        alert
                    )

                    print(

                        f"Alert created: {wallet}"

                    )


            balance_record = Balance(

                wallet_address=
                wallet,

                token_address=
                settings.TOKEN_ADDRESS,

                balance=
                balance

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