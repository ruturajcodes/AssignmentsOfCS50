import sys

def convert(fract):
    while True:
        try:
            cut = fract.split("/")
            x = int(cut[0])
            y = int(cut[1])
            frr = x/y
            if frr <=1 :
                nans = frr*100
                return round(nans)
            else:
                fract = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(perc):
    if perc>=99:
        return "F"
    elif perc<=1:
        return "E"
    else:
        return f"{perc}%"



def main():
    fract = input("Fraction: ")
    perc = convert(fract)
    tbp = gauge(perc)
    print(tbp)






    # ans = gauge(perc)
    # print(ans)






if __name__ == "__main__":
    main()
