"""
Таблица для БД Сотрудники
1. id - уникальный номер в БД.
2. email - адрес, обязательный.
3. last_name - фамилия, обязательно.
4. first_name - имя, обязательно.
5. patronymic - отчество, необязательное.
6. post - должность, необязательное (?).
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(40), nullable=False, unique=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    patronymic = Column(String(50))
    post = Column(String(50))
