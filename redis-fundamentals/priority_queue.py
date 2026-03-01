"""
Priority Queue backed by a Redis SORTED SET.

Design:
  - Each task is a member in a SORTED SET.
  - The score is the priority (higher score = higher priority).
  - ZPOPMAX atomically dequeues the highest-priority task.
  - ZADD with the same task name updates its priority (re-prioritization is free).

Key Redis commands used:
  ZADD   key score member   — enqueue (or update priority)
  ZPOPMAX key               — dequeue highest-priority task
  ZRANGE key 0 -1 WITHSCORES — inspect queue (lowest → highest)
  ZCARD  key                — queue length
  ZSCORE key member         — check a specific task's priority
"""

import redis

r = redis.Redis(host="localhost",port=6379,decode_responses=True)
r.set("summerinternship","highest_priority")
result = r.get("summerinternship")
print(result)  # Output: you

def queue_length(key):
    return r.zcard(key)

def enqueue(key,score,member):
    """Enqueue a task with a given priority."""
    try:
        r.zadd(key, {member: score})
        print(f"Added {member} with priority {score} in {key}")
    except Exception as e:
        print(f"{e}")
        

def dequeue(key):
    """Dequeue a task with the highest priority"""
    if queue_length(key) != 0:
        return r.zpopmax(key)
    else:
        print(f"Priority Queue {key} is already empty")

def inspect_queue(key):
    """Return all tasks including the scores"""
    return r.zrange(key,0,-1,withscores=True)


if __name__=="__main__":
    #1. Pushing some names onto bb273 key
    enqueue("bb273", 3 ,"sumanthra")
    enqueue("bb273",4,"rithvik")
    enqueue("bb273",2,"nishanth")
    enqueue("bb273",1,"sharath")
    enqueue("bb273",5,"sushma")

    #2. printing the queue
    print("Printing from youngest to eldest (before reprioritization): ",inspect_queue("bb273"))

    # 3. Reprioritizing one member midflight
    enqueue("bb273",0,"rithvik") #Cuz rithvik == err
    print("Printing from youngest to eldest (After reprioritization): ",inspect_queue("bb273"))
    #4. Draining hte queue completely
    while queue_length("bb273") != 0:
        print(dequeue("bb273"))
        



