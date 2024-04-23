from src.db import database

from tasks.model import Task
from tasks.schema import TaskSchema

async def add_task(payload: TaskSchema):
    query = Task.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_tasks():
    query = Task.select()
    return await database.fetch_all(query=query)


async def get_task(id):
    query = Task.select(Task.c.id == id)
    return await database.fetch_one(query=query)


async def delete_task(id: int):
    query = Task.delete().where(Task.c.id == id)
    return await database.execute(query=query)


async def update_task(id: int, payload: TaskSchema):
    query = (
        Task
        .update()
        .where(Task.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
