"""
Файл с сервисными функциями по Заданиям.
Пробуем реализовать CRUD.
1. Получение данных по всем заданиям.
2. Добавление нового задания.
3. Редактирование данных о задании.
4. Удаление данных задания.
5. Чтение данных об одном задании
"""

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session

from src.db import get_db
from tasks.model import Task
from tasks.schema import TasksList, TaskCreateUpdateSchema

api_task = APIRouter(tags=['Tasks'], prefix='/tasks')


@api_task.get('/', response_model=TasksList)
def get_tasks(db: Session = Depends(get_db),
              limit: int = 10, page: int = 1) -> dict:
    skip = (page - 1) * limit
    tasks = db.query(Task).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(tasks), 'tasks': tasks}


@api_task.get('/get/{taskId}')
def get_task(taskId: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == taskId).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Задание с id: {taskId} не найдено')
    return {"status": "success", "task": task}


@api_task.post('/create/', status_code=status.HTTP_201_CREATED)
def create_tasks(payload: TaskCreateUpdateSchema = Depends(),
                 db: Session = Depends(get_db)):
    new_task = Task(**payload.dict())
    if new_task.employee_id is not None and new_task.status == 0:
        new_task.status = 1
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {'status': 'success',
            'task': new_task}


@api_task.patch('/update/{taskId}')
def update_task(taskId: str, payload: TaskCreateUpdateSchema = Depends(),
                db: Session = Depends(get_db)):
    task_query = db.query(Task).filter(Task.id == taskId)
    task = task_query.first()
    print(task)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Задание с id: {taskId} не найдено')
    update_data = payload.dict(exclude_unset=True)
    task_query.filter(Task.id == taskId).update(
        update_data, synchronize_session=False)
    db.commit()
    db.refresh(task)
    return {"status": "success", "task": task}


@api_task.delete('/del/{taskId}')
def delete_task(taskId: str, db: Session = Depends(get_db)):
    task_query = db.query(Task).filter(Task.id == taskId)
    task = task_query.first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Задание с id: {taskId} не найдено')
    task_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@api_task.get('/important')
def get_important_tasks(db: Session = Depends(get_db),
                        limit: int = 10, page: int = 1):
    """
    Получить важные задачи
    Читаем по статусу задачи = 0, потом проверяем есть ли родитель
    :param db: указатель на БД
    :param limit: количество задач на страницу
    :param page: номер страницы
    :return: пока словарь: статус успешно, результат, список задач
    """
    skip = (page - 1) * limit
    tasks = (db.query(Task).filter(Task.status == 0).
             limit(limit).offset(skip).all())
    tasks_ret = []
    for task in tasks:
        if task.parent_task is not None:
            print(task.parent_task)
        if task.parent_id is not None:
            tasks_ret.append(task)

    return {'status': 'success', 'results': len(tasks_ret), 'tasks': tasks_ret}


@api_task.get('/free')
def get_free_tasks(db: Session = Depends(get_db),
                   limit: int = 10, page: int = 1):
    """
    Получить незадействованные задания
    Читаем по статусу задачи = 0
    :param db: указатель на БД
    :param limit: количество задач на страницу
    :param page: номер страницы
    :return: пока словарь: статус успешно, результат, список задач
    """
    skip = (page - 1) * limit
    tasks = (db.query(Task).filter(Task.status == 0).
             limit(limit).offset(skip).all())

    return {'status': 'success', 'results': len(tasks), 'tasks': tasks}
