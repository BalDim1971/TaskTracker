"""
Таблица для БД Задания
1. id - уникальный идентификатор в БД.
2. name - наименование задания, уникальное, обязательное.
3. content - содержание задания, обязательное.
4. period_of_execution - срок выполнения дата+время ?
5. parent_id - ссылка на родительскую задачу.
6. status - статус выполнения задачи, пока: 0 - ждет исполнителя, 1 - в работе
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Task(Base):
    __tablename__ = 'task',
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    period_of_execution = Column(DateTime(timezone=True),
                                 server_default=func.now())
    parent_id = Column(ForeignKey('task.id'), nullable=True)
    status = Column(Integer, nullable=False, default=0)
    employee_id = Column(ForeignKey('public.employee.id'))
