from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from sqlalchemy.sql import func

from app.database.session import Base


class Balance(Base):

    __tablename__ = "balances"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    wallet_address = Column(
        String,
        nullable=False
    )

    token_address = Column(
        String,
        nullable=False
    )

    balance = Column(
        Float,
        nullable=False
    )

    collected_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )