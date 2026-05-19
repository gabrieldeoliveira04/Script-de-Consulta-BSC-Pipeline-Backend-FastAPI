from config.settings import settings
from database.connection import engine


print(engine)

print(settings.DATABASE_URL)

print(settings.RPC_URL)

print(settings.WALLETS)