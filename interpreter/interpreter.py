def main():
    get_expression()


def get_expression():
    expression = input("Expression: ").strip().split(" ")
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])

    """
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    """

    if y == "+":
        print(float(round(x+z,1)))
    elif y == "-":
        print(float(round(x-z,1)))
    elif y == "*":
        print(float(round(x*z,1)))
    elif y == "/" and z!=0:
        print(float(round(x/z,1)))

main()