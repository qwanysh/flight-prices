from peewee import SqliteDatabase

import config

db = SqliteDatabase(config.DATABASE_URL)
