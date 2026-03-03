import redis
import json
from typing import Any

r = redis.Redis(host="localhost",port=6379,decode_responses=True)

def add(a:int,b:int) -> int:
    return a + b

REGISTRY = {
    "add": add
}

def deserialization(task:str) -> Any:
    deserialized_task = json.loads(task)
    task_id = deserialized_task["task_id"]
    func = REGISTRY[deserialized_task["task"]]
    result = func(*deserialized_task["args"],**deserialized_task["kwargs"])
    return task_id,result


while True:
    serz_task = r.blpop("tasks_queue")
    print(f"Popped task from the message queue: {serz_task}")
    _, raw_task = serz_task
    task_id,result = deserialization(raw_task)
    result_key = f"result:{task_id}"
    r.set(result_key,result)
    print(task_id,result)