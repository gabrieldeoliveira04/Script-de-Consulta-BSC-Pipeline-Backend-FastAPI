from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from app.database.session import Base


class Alert(Base):

    __tablename__ = "alerts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    wallet_address = Column(
        String,
        nullable=False
    )

    previous_balance = Column(
        Float,
        nullable=False
    )

    current_balance = Column(
        Float,
        nullable=False
    )

    variation_percent = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )