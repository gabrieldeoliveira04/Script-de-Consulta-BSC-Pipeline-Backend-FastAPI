from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from app.collector.balance_collector import (
    collect_balances
)


scheduler = BackgroundScheduler()


def start_scheduler():

    scheduler.add_job(
        collect_balances,

        trigger="interval",

        minutes=1,

        id="wallet_collector",

        replace_existing=True
    )

    scheduler.start()

    print(
        "Collector scheduler started"
    )