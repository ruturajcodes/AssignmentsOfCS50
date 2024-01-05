def main():
    time = input("What time is it? ").strip()

    value = convert(time)
    if 7 <= value <= 8:
        print("breakfast time")
    elif 12 <= value <= 13:
        print("lunch time")
    elif 18 <= value <= 19:
        print("dinner time")



def convert(time):
    time_ct = time.split(":")
    hrs = float(time_ct[0])
    minutes = float(time_ct[1])
    value = hrs+round(minutes/60,2)
    # print(hrs+round(minutes/60,2))
    return value


if __name__ == "__main__":
    main()