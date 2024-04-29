import uvicorn
from uuid import UUID
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, joinedload

from src.config import DB_HOST
from src.services import create_db
from src.db import engine
from src.db import get_db

from employee.model import Base, Employee
from employee.services import api_employee

from tasks.model import Task
from tasks.schema import TasksList
from tasks.services import api_task

create_db()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Трекер задач сотрудников",
)

app.include_router(api_employee, tags=['Employees'], prefix='/employees')
app.include_router(api_task, tags=['Tasks'], prefix='/tasks')


@app.get('/')
def root(db: Session = Depends(get_db)):
    employees = db.query(Employee).options(joinedload(Employee.tasks)).all()
    for employee in employees:
        print(employee)
        print(employee.count_task())
    return {'status': 'success',
            'results': len(employees),
            'employees': employees}


@app.get('/important/')
def get_important_tasks(db: Session = Depends(get_db),
                        limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    tasks = (db.query(Task).filter(Task.status == 0).
             limit(limit).offset(skip).all())
    for task in tasks:
        if task.parent_id is None:
            print(task)
    
    return {'status': 'success', 'results': len(tasks), 'tasks': tasks}


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host=DB_HOST, port=8000)
