from databases import Database
from sqlalchemy import Column, Integer, String, Table, MetaData

import twitch_dungeon.settings as settings


database = Database(settings.config["DATABASE_URL"])


metadata = MetaData()

characters = Table(
    "characters",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("level", Integer),
    Column("STR", Integer),
    Column("DEX", Integer),
    Column("CON", Integer),
    Column("WIS", Integer),
    Column("INT", Integer),
)

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("desc", String),
    Column("cost", String),
    Column("caller", String),
    Column("command", String),
)