def main():
    greeting = input("Greeting: ")
    verification(greeting.strip().lower())

def verification(greet_msg):
    if("hello" in greet_msg):
        print("$0")
    elif(greet_msg[0] == "h"):
        print("$20")
    else:
        print("$100")

main()