from fastapi import FastAPI

from app.handlers import connect_to_db, update_flights
from app.routers import api

app = FastAPI()
app.include_router(api.router, prefix='/flights')

app.add_event_handler('startup', connect_to_db)
app.add_event_handler('startup', update_flights)
