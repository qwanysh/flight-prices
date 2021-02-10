from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict

from app.models import Flight

router = APIRouter()


@router.get('/')
def get_flights():
    flights = Flight.select()
    return [model_to_dict(flight) for flight in flights]
