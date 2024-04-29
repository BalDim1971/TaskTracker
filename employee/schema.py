"""
Файл со схемой Сотрудник
"""
from typing import List
from pydantic import BaseModel, EmailStr


class EmployeeSchema(BaseModel):
    """
    Схема Сотрудник.
    Без uuid
    """
    email: EmailStr
    last_name: str
    first_name: str
    patronymic: str | None = None
    post: str | None = None

    class Config:
        from_attributes = True
        population_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "email": "example@test.com",
                "last_name": "Иванов",
                "first_name": "Иван",
                "patronymic": "Иванович",
                "post": "Инженер"
            }
        }


class EmployeeList(BaseModel):
    """
    Список заданий
    """
    employees: List[EmployeeSchema]
