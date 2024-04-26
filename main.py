import uvicorn
from fastapi import FastAPI

from src.config import DB_HOST
from src.services import create_db
from src.db import database, engine

from employee.model import Base, Employee
from employee.services import employees

from tasks.model import Task
from tasks.services import tasks

import sqlalchemy as sa

create_db()

Base.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


# @app.get("/")
# async def read_tasks_employees(skip: int = 0, limit: int = 10):
#     questions = sa.query(Task).filter(
#         Task.topic_id == t1_id,
#     ).order_by(Question.id.desc()).limit(10).all()


app.include_router(employees)
app.include_router(tasks)

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host=DB_HOST, port=8000)
