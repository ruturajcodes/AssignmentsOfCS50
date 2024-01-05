import csv

students = []

def new_fun():
    '''this is check function'''

with open("students.csv") as file:
    line = csv.DictReader(file)
    for row in line:
        students.append({"name":row['name'],"home":row['home'],"house":row['house']})

for lin in sorted(students, key = lambda students: students["name"]):
    print(f"{lin['name']} is in {lin['home']}")

# print("type of students : ",type(line))