import inflect
import sys
p1 = inflect.engine()

i = 0
raja=[]
while True:
    try:
        name = input("Name: ")
        raja.insert(i,name)
        i = i + 1

# 
# or
# raja=[]
# while True:
#     try:
#         name = input("Name: ")
#         raja.append(name)


    except EOFError:
        print("Adieu, adieu, to",p1.join(raja))
        sys.exit()

