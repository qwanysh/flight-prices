import config
from app.models import Route, Flight
from app.utils.flights_checker import FlightsChecker
from db import db


async def update_flights():
    checker = FlightsChecker(config.ROUTES_LIST)
    await checker.run()


def connect_to_db():
    db.create_tables([Route, Flight])
