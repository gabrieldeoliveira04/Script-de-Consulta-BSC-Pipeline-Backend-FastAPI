from database.connection import engine
from database.session import Base

from models.balance import Balance


print("Creating database tables...")


Base.metadata.create_all(
    bind=engine
)


print("Tables created successfully")