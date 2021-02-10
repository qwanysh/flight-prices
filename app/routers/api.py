from fastapi import APIRouter

from app.utils.helpers import get_grouped_routes_with_price

router = APIRouter()


@router.get('/')
def get_flights():
    return get_grouped_routes_with_price()
