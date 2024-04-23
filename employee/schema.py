"""
Файл с моделью данных Сотрудник
"""

from typing import List, Optional
from pydantic import BaseModel


class EmployeeSchema(BaseModel):
    email: str
    last_name: str
    first_name: str
    patronymic: str
    post: str
