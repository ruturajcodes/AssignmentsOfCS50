import random


def main():
    level = get_level()

    score = gamestart(level)
    print("Score:",score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            available = [1,2,3]
            if level not in available:
                continue
            else:
                return level
                break
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)

    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y



def trial(x,y):
    chance = 1
    while chance<=3:
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans == (x+y):
                return True
            else:
                chance = chance + 1
                print("EEE")
        except:
            chance = chance + 1
            print("EEE")
    if ans != (x+y):
        print(f"{x} + {y} = {x+y}")


def gamestart(level):
    round = 1
    score = 0
    while round<=10:
        x,y = generate_integer(level)
        myans = trial(x,y)
        if myans == True:
            score= score + 1
        round = round + 1
    return score

if __name__ == "__main__":
    main()