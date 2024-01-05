def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    check(answer.strip().lower())

def check(str_verify):
    if(str_verify == "42" or str_verify == "forty-two" or str_verify == "forty two"):
        print("Yes")
    else:
        print("No")

main()
