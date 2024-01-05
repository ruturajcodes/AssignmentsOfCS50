
# address = input("IPv4 Address: ")





import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
        lon = ip.split(".")
        count = 0
        # print(lon)
        # print(int(lon[1]))
        for i in range(len(lon)):
            if int(lon[i]) < 256:
                count = count + 1
                continue
            else:
                return False
        if count == len(lon):
            return True



        # return "True"
    else:

        return False





if __name__ == "__main__":
    main()