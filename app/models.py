from datetime import datetime

from peewee import (
    Model, CharField, ForeignKeyField, DateTimeField, IntegerField,
)

from db import db


class BaseModel(Model):
    class Meta:
        database = db


class Route(BaseModel):
    fly_from = CharField()
    fly_to = CharField()

    def __str__(self):
        return f'{__class__.__name__}({self.fly_from}-{self.fly_to})'

    class Meta:
        table_name = 'routes'


class Flight(BaseModel):
    route = ForeignKeyField(Route, backref='flights')
    price = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'flights'
