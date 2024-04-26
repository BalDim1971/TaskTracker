"""
Файл с моделью данных Задание
"""
from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class TaskSchema(BaseModel):
    name: str
    content: str
    period_of_execution: Optional[datetime] = None
    parent_id: Optional[int] = None
    status: int = 0
    employee_id: Optional[int] = None
