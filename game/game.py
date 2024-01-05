from random import choice
import sys
while True:
    try:
        level = int(input("Level: "))
        if level<=0:
            continue
        else:
            break
    except (TypeError, ValueError):
        pass

ans = choice(range(1,(level+1)))

while True:
    try:
        guess = int(input("Guess: "))
        if guess<0:
            continue
        elif guess<ans:
            print("Too small!")
            continue
        elif guess>ans:
            print("Too large!")
            continue
        elif guess == ans:
            print("Just right!")
            sys.exit(0)

    except (TypeError, ValueError):
        pass
