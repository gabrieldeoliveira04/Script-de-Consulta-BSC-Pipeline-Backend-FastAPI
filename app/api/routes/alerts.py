from fastapi import APIRouter

from app.database.session import (
    SessionLocal
)

from app.models.alert import (
    Alert
)


router = APIRouter(

    prefix="/alerts",

    tags=["Alerts"]

)


@router.get(

    "",

    summary="Get recent alerts",

    description="Returns latest wallet variation alerts"

)

def get_alerts():

    db = SessionLocal()

    try:

        alerts = (

            db.query(Alert)

            .order_by(

                Alert.created_at.desc()

            )

            .limit(20)

            .all()

        )

        return alerts

    finally:

        db.close()