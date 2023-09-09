from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
)

products = Table(
    "products",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('name', String, nullable=False),
    Column('text', String, nullable=True),
    Column('price', Integer, nullable=False),
)