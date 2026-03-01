import redis
r = redis.Redis(host="localhost",port=6379,decode_responses=True)

def publish(channel,message):
    r.publish(channel,message)


if __name__=="__main__":
    
    while True:
        user_input = input("Enter a value (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break  # Exit the loop if the user types 'quit'
        # Process the input here
        publish("events",user_input)
        print(f"You entered: {user_input}")

    print("Program ended.")
