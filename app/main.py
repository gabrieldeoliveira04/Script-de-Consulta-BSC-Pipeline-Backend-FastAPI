from database.connection import engine
from database.session import Base

from models.balance import Balance


from collector.balance_collector import (
    collect_balances
)


collect_balances()