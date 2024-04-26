from src.db import database
from employee.model import Employee
from employee.schema import EmployeeSchema


async def add_employee(payload: EmployeeSchema):
    query = Employee.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_employees():
    query = Employee.select()
    return await database.fetch_all(query=query)


async def get_employee(id):
    query = Employee.select(Employee.c.id == id)
    return await database.fetch_one(query=query)


async def delete_employee(id: int):
    query = Employee.delete().where(Employee.c.id == id)
    return await database.execute(query=query)


async def update_employee(id: int, payload: EmployeeSchema):
    query = (
        Employee
        .update()
        .where(Employee.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
