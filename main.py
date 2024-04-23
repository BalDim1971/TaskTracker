import uvicorn
from fastapi import FastAPI

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
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(employees)
app.include_router(tasks)

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host=DB_HOST, port=8000)
