"""
Таблица для БД Задания
1. id - уникальный идентификатор в БД.
2. name - наименование задания, уникальное, обязательное.
3. content - содержание задания, обязательное.
4. period_of_execution - срок выполнения дата+время ?
5. parent_id - ссылка на родительскую задачу.
6. status - статус выполнения задачи, пока: 0 - ждет исполнителя, 1 - в работе
"""

from sqlalchemy import (Column, Integer, MetaData, String, Table, Text,
                        ForeignKey, DateTime)

metadata_task = MetaData()

Task = Table(
    'task',
    metadata_task,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False, unique=True),
    Column('content', Text, nullable=False),
    Column('period_of_execution', DateTime, nullable=False),
    Column('parent_id', ForeignKey('task.id'), nullable=True),
    Column('status', Integer, nullable=False, default=0)

)
