# create empty dictionary
gc_list = {}

while True:
    try:
        # user input
        glist = input()
        # check if item present in list
        if glist in gc_list:
            gc_list[glist] = gc_list[glist] + 1
           # if present then add 1 to count
        else:
            gc_list[glist] = 1
        # otherwise add the item for the first time
    except EOFError:
        # print all the items in alphabetical order
        for i in sorted(gc_list.keys()):
            print(f"{gc_list[i]}",i.upper())
        # stop the loop
        break