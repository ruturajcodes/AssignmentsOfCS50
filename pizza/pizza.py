import sys
import csv
from tabulate import tabulate

students = []


def main():
    check_the_file()
    try:
        with open(sys.argv[1],"r") as file:
            reader= csv.reader(file)
            for row in reader:
                students.append(row)

            print(students)
            # print(reader)
            print(tabulate(students[1:], headers=students[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")




def check_the_file():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) >=3:
        sys.exit("Too many command-line arguments")

    elif not ".csv" in sys.argv[1]:
            sys.exit("Not a CSV file ")


if __name__ == "__main__":
    main()