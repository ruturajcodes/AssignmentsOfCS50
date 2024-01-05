def calc_per(x1, y1):
    perc = round((x1/y1)*100)

    if perc >= 99:
        return "F"
    elif perc <= 1:
        return "E"
    else:
        return perc
    return



def main():
    while True:
        try:
            fract = input("Fraction: ").split("/")
            x = int(fract[0])
            y = int(fract[1])
            frr = x/y
            if frr<=1:
                break
        except (ValueError,ZeroDivisionError):
            pass

    frr = frr*100

    if frr>=99:
        print("F")
    elif frr<=1:
        print("E")
    else:
        print(f"{round(frr)}%")


main()
