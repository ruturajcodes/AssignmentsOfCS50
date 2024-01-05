def main():
    greeting = input("Greeting: ")
    amt = value(greeting.strip().lower())
    print(amt)

def value(greeting):
    if("hello" in greeting):
        # print("$0")
        return 0
    elif(greeting[0] == "h"):
        # print("$20")
        return 20
    else:
        # print("$100")
        return 100

if __name__ == "__main__":
    main()
