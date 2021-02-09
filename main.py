from fastapi import FastAPI

from app import api
from app.handlers import connect_to_db, update_flights

app = FastAPI()
app.include_router(api.router, prefix='/flights')

app.add_event_handler('startup', update_flights)
app.add_event_handler('startup', connect_to_db)
