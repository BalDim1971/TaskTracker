import uvicorn
from fastapi import FastAPI
# from sqlalchemy import select

from src.config import DB_HOST
from src.services import create_db
from src.db import database, engine

from employee.model import metadata_employee
from employee.services import employees

from tasks.model import metadata_task
from tasks.services import tasks

create_db()

metadata_employee.create_all(engine)
metadata_task.create_all(engine)

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
# async def read_root():
#     # изменим роут таким образом, чтобы он брал данные из БД
#     query = (
#         select(
#             [
#                 posts_table.c.id,
#                 posts_table.c.created_at,
#                 posts_table.c.title,
#                 posts_table.c.content,
#                 posts_table.c.user_id,
#                 users_table.c.name.label("user_name"),
#             ]
#         )
#         .select_from(posts_table.join(users_table))
#         .order_by(desc(posts_table.c.created_at))
#     )
#     return await database.fetch_all(query)


app.include_router(employees)
app.include_router(tasks)

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host=DB_HOST, port=8000)
