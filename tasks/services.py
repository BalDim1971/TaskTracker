"""
Файл с сервисными функциями по Заданиям.
Пробуем реализовать CRUD.
1. Получение данных по всем заданиям.
2. Добавление нового задания.
3. Редактирование данных о задании.
4. Удаление данных задания.
5. Чтение данных об одном задании
"""

from typing import List
from fastapi import APIRouter, HTTPException, Depends

from tasks.schema import TaskSchema
from tasks import db_manager

tasks = APIRouter()


@tasks.get('/task/', response_model=List[TaskSchema])
async def index():
    return await db_manager.get_all_tasks()


@tasks.post('/task/', status_code=201)
async def add_task(payload: TaskSchema = Depends()):
    task_id = await db_manager.add_task(payload)
    response = {
        'id': task_id,
        **payload.dict()
    }
    
    return response


@tasks.put('/task/{id}')
async def update_task(id: int, payload: TaskSchema = Depends()):
    task = await db_manager.get_task(id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    update_data = payload.dict(exclude_unset=True)
    task_in_db = TaskSchema(**task)
    
    updated_task = task_in_db.copy(update=update_data)
    
    return await db_manager.update_task(id, updated_task)


@tasks.delete('/task/{id}')
async def delete_task(id: int):
    task = await db_manager.get_task(id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return await db_manager.delete_task(id)
