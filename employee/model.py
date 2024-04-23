"""
Таблица для БД Сотрудники
1. id - уникальный номер в БД.
2. email - адрес, обязательный.
3. last_name - фамилия, обязательно.
4. first_name - имя, обязательно.
5. patronymic - отчество, необязательное.
6. post - должность, необязательное (?).
"""

from sqlalchemy import (Column, Integer, MetaData, String, Table)

metadata_employee = MetaData()

Employee = Table(
    'employee',
    metadata_employee,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('email', String(50), nullable=False, unique=True),
    Column('last_name', String(50), nullable=False),
    Column('first_name', String(50), nullable=False),
    Column('patronymic', String(50)),
    Column('post', String(50))
)
