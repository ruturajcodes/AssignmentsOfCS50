import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

if len(sys.argv) == 1:
    rand_font = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font" ):
    rand_font = False
else:
    sys.exit(1)

mystr = input("Input: ")

if rand_font == False:
    try:
        nfont = figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)

else:
    nfont = choice(figlet.getFonts())
    figlet.setFont(font=nfont)
# mystr = input("Input: ")

print("Output: ")
print(figlet.renderText(mystr))











# try:
#     if sys.argv[1] == "-f":
#         if sys.argv[2] in figlet.getFonts():
#             mystr = input("Input: ")
#             figlet.setFont(font=sys.argv[2])
#             print(figlet.renderText(mystr))

#     elif sys.argv[1] == "":
#         mystr = input("Input: ")
#         rand_font = choice(figlet.getFonts())     #choice() function from "random" module takes list as an argument
#         figlet.setFont(font=rand_font)
#         print(figlet.renderText(mystr))

# except IndexError:
#     sys.exit("Invalid usage")




# # print(figlet.getFonts(),end="\n")
# rand_font = choice(figlet.getFonts())