"""
Таблица для БД Задания
1. id - уникальный идентификатор в БД.
2. name - наименование задания, уникальное, обязательное.
3. content - содержание задания, обязательное.
"""

from sqlalchemy import (Column, Integer, MetaData, String, Table, Text)

metadata_task = MetaData()

Task = Table(
    'task',
    metadata_task,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False, unique=True),
    Column('content', Text, nullable=False)
)
