from peewee import CharField

from .base_model import BaseModel


class Route(BaseModel):
    fly_from = CharField()
    fly_to = CharField()

    class Meta:
        table_name = 'routes'
