import string
from models import *
from helpers.utils import object_as_dict
from celery_tasks import *
import os
from config import UPLOAD_FOLDER

def get_all_tasks_by_user(user_id: int):
    message: list = []
    status: int = 200

    try:
       tasks = Task.get_by_user_id(user_id)

       for i in range(len(tasks)):
            task = object_as_dict(tasks[i])
            message.append(task)

    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message , 'status': status }


def create_new_task(user_id, upload_file, new_format):
    message: str = ''
    status: int = 200

    try:
        new_task = Task(upload_file.filename, user_id, new_format)
        new_task.save()

        create_file(upload_file, new_task.id, user_id)
    
        message = f'Task for change the extension of file: {upload_file.filename} to {new_format} was created'
       
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }


def get_task_by_id(id_task: int):
    message: str = ''
    status: int = 200

    try:
        task = Task.get_by_id(id_task)
        message = object_as_dict(task)
        
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }

def get_all_uploaded_tasks():
    message: list = []
    status: int = 200

    try:
       tasks = Task.get_by_uploaded()

       for i in range(len(tasks)):
            task = object_as_dict(tasks[i])
            message.append(task)

    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }

# def put_change_extension(id_task: int, extension: string):
#     message: str = ''
#     status: int = 200

#     try:
#         task = Task.get_by_id(id_task)
#         message = object_as_dict(task)
        
#     except Exception as e:
#         status = 500
#         message = f'Error: {e}'
    

#     try:
#         nameTask = task.file_name.split('.')[0]
#         os.rename(UPLOAD_FOLDER+"/"+task.file_name, UPLOAD_FOLDER+"/"+nameTask+"."+extension)
#     except Exception as e:
#         status = 500
#         message = f'Error: {e}'


#     return { 'message': message, 'status': status }