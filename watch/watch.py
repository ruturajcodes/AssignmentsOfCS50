import re
import sys


def main():
    uid = parse(input("HTML: "))
    if uid != None:
        print(uid)
    elif uid == None:
        print(None)


def parse(s):
    matches = re.search(r"\"https?://(www\.)?youtube.com/embed/(.{11})\" ?",s, re.IGNORECASE)
    if matches:
        # print(re.search(r"\"https?://(www\.)?youtube.com/embed/.*\" ?",s, re.IGNORECASE))
        return f"https://youtu.be/{matches.group(2).strip()}"
    else:
        return None








if __name__ == "__main__":
    main()