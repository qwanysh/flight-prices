from datetime import datetime

from peewee import ForeignKeyField, IntegerField, DateTimeField

from app.models.route import Route
from .base_model import BaseModel


class Flight(BaseModel):
    route = ForeignKeyField(Route, backref='flights', on_delete='CASCADE')
    price = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'flights'
