import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ummm = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(ummm)



if __name__ == "__main__":
    main()