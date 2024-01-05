import sys

try:
    if ".py" in sys.argv[1]:
        if len(sys.argv) == 2:
            with open(sys.argv[1],"r") as file:
                lines = file.readlines()

            count = 0

            for line in lines:
                if line.isspace() or line.lstrip().startswith("#"):
                    continue
                else:
                    count = count + 1
        elif len(sys.argv) >= 3:
            sys.exit("Too many command-line arguments")
    else:
        sys.exit("Not a Python file")


    print(count)
    # print("Type of line:",line[0:])
except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")