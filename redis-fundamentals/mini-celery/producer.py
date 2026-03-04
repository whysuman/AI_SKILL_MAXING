import json
import redis
from pydantic import BaseModel, Field
from uuid import uuid4, UUID
import time

class Task(BaseModel):
    name: str
    task_id: UUID = Field(default_factory=uuid4)
    args:list
    kwargs:dict


r = redis.Redis(host='localhost',port=6379,decode_responses=True)

#TASK Pydantic model to STRING coversion
def task_serializer(task_message:Task) -> str:
    json_task = {
            "task": task_message.name,
            "task_id" : str(task_message.task_id),
            "args": task_message.args, 
            "kwargs": task_message.kwargs
        }

    serialized_str = json.dumps(json_task)
    r.rpush("tasks_queue",serialized_str)   
    r.hset(f"result:{json_task["task_id"]}",mapping={"status":"PENDING"}) 

    return serialized_str


if __name__ == "__main__":
    task = Task(name="add",args=[3,7],kwargs={})
    serz_task = task_serializer(task)
    print(f"Enqueued: {serz_task}")
    while True:
        res = r.hgetall(f"result:{str(task.task_id)}")
        if res["status"] in ("SUCCESS", "FAILURE"):
            print(res)
            break
        else:
            time.sleep(1.0)

