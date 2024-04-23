"""
Файл с моделью данных Задание
"""

from pydantic import BaseModel


class TaskSchema(BaseModel):
    name: str
    content: str
