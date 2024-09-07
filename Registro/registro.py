from typing import Union
from fastapi import FastAPI
from typing import List
from models.log_model import LogModel
import json
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#ruta para meter nuevos logs de los procesos
@app.post('/newlog')
def log_container(logProcess: List[LogModel]):
    log_file = 'logs/logs_register.json'

    if os.path.exists(log_file):
        with open(log_file,'r') as file:
            existing_logs = json.load(file)
    else:
        existing_logs = []

    nuevos_logs = [log.dict() for log in logProcess]
    existing_logs.extend(nuevos_logs)

    with open(log_file, 'w') as file:
        json.dump(existing_logs, file, indent=4)

    return{"Response": "Ok"}
