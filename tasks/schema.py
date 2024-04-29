"""
Файл с моделью данных Задание
"""
from uuid import UUID
from datetime import datetime
from typing import List
from pydantic import BaseModel


class TaskSchema(BaseModel):
    """
    Схема Задание.
    Без uuid
    """
    name: str
    content: str
    period_of_execution: datetime | None = None
    parent_id: UUID | None = None
    status: int = 0
    employee_id: UUID | None = None

    class Config:
        from_attributes = True
        population_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "name": "Задание1",
                "content": "Описание задания",
                "period_of_execution": "2024-04-28 19:35:00+03:00",
                "status": "0"
            }
        }


class TasksList(BaseModel):
    """
    Список заданий
    """
    tasks: List[TaskSchema]
