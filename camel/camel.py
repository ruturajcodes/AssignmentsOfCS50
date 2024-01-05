case1 = input("camelCase: ")
def snake_case(case1):
    print("snake_case: ", end="")
    for i in case1:
        if i.isupper():
            print("_"+i.lower(), end="")
        else:
            print(i, end="")
    print()

snake_case(case1)