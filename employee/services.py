"""
Файл с сервисными функциями по Сотрудникам.
Пробуем реализовать CRUD.
1. Получение данных по всем сотрудникам.
2. Добавление нового сотрудника.
3. Редактирование данных о сотруднике.
4. Удаление данных сотрудника.
5. Чтение данных об одном сотруднике
"""

from typing import List
from fastapi import APIRouter, HTTPException, Depends

from employee.schema import EmployeeSchema
from employee import db_manager

employees = APIRouter()


@employees.get('/employee/', response_model=List[EmployeeSchema])
async def index():
    return await db_manager.get_all_employees()


@employees.post('/employee/', status_code=201)
async def add_employee(payload: EmployeeSchema = Depends()):
    employee_id = await db_manager.add_employee(payload)
    response = {
        'id': employee_id,
        **payload.dict()
    }
    
    return response


@employees.put('/employee/{id}')
async def update_employee(id: int, payload: EmployeeSchema = Depends()):
    employee = await db_manager.get_employee(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    
    update_data = payload.dict(exclude_unset=True)
    employee_in_db = EmployeeSchema(**employee)
    
    updated_employee = employee_in_db.copy(update=update_data)
    
    return await db_manager.update_employee(id, updated_employee)


@employees.delete('/employee/{id}')
async def delete_employee(id: int):
    employee = await db_manager.get_employee(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    return await db_manager.delete_employee(id)
