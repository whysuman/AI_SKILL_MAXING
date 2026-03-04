import redis
import json
from typing import Any

r = redis.Redis(host="localhost",port=6379,decode_responses=True)

def add(a:int,b:int) -> int:
    return a + b

REGISTRY = {
    "add": add
}

def deserialization(task:str) -> dict:
    deserialized_task = json.loads(task)
    return deserialized_task

def execute_task(task:dict) -> Any:
    func = REGISTRY[task["task"]]
    result = func(*task["args"],**task["kwargs"])
    return result

while True:
    serz_task = r.blpop("tasks_queue")
    _, raw_task = serz_task
    print(f"Popped task from the message queue: {serz_task}")
    #Parsing RAW STRING into a JSON TASK
    parsed_task = deserialization(raw_task)
    result_key = f"result:{parsed_task["task_id"]}"
    #Set the task status to STARTED before executing the task
    r.hset(result_key,mapping={"status": "STARTED"})
    try:
        result = execute_task(parsed_task)
        r.hset(result_key,mapping={"status": "SUCCESS","result": result,"error":""})
    except Exception as e:
        r.hset(result_key,mapping={"status": "FAILURE","result": "","error":f"{e}"})
    # print(task_id,result)