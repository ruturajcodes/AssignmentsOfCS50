total = 50
due = total

while True:
    inp1 = int(input("Insert Coin: "))
    if inp1 == 25 or inp1 == 10 or inp1 == 5:
        rem = due - inp1
        if rem == 0:
            print("Change Owed: 0")
            break
        elif rem > 0:
            due = rem
            print("Amount Due:", rem)
            continue
        elif rem < 0:
            print("Change Owed:", rem*(-1))
            break
    else:
        print("Amount Due:", due)
        continue
