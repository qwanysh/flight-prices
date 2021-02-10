import config
from app.models import Flight, Route

from app.utils.flights_checker import FlightsChecker
from app.db import db


async def update_flights():
    await FlightsChecker(config.ROUTES_LIST).run()


def connect_to_db():
    db.create_tables([Route, Flight])
