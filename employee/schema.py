"""
Файл со схемой Сотрудник
"""

from typing import Optional
from pydantic import BaseModel, EmailStr


class EmployeeSchema(BaseModel):
    """
    Схема Сотрудник.
    """
    email: EmailStr
    last_name: str
    first_name: str
    patronymic: Optional[str] = None
    post: Optional[str] = None
