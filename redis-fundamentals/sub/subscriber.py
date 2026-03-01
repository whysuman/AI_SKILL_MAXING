import redis

r = redis.Redis(host="localhost",port=6379,decode_responses=True)



def subscribe_channel(subscriber,channel):
    subscriber.subscribe(channel)
    
def unsubscribe_channel(subscriber,channel=None):
    if channel==None:
        subscriber.unsubscribe()
    subscriber.unsubscribe(channel)


if __name__=="__main__":
    subscriber = r.pubsub()
    subscribe_channel(subscriber=subscriber,channel="events")
    for message in subscriber.listen():
        print(f"Received message: {message}")
        if message["data"] == "quit":
            unsubscribe_channel(subscriber=subscriber,channel="events")