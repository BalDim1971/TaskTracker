"""
Файл с моделью данных Задание
"""
from datetime import datetime

from pydantic import BaseModel


class TaskSchema(BaseModel):
    name: str
    content: str
    period_of_execution: datetime
    parent_id: int
    status: int
