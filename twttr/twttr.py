

def main():
    word = input("")
    # ans = []
    main_ans = shorten(word)

    print(main_ans)
def shorten(word):
    ans = []
    for i in range(len(word)):
        if word[i] == "a" or word[i] =="A" or word[i] =="e" or word[i] == "E" or word[i] =="i" or word[i] =="I" or word[i] =="o" or word[i] =="O" or word[i] =="u" or word[i] =="U":
            continue
        else:
            ans.insert(i,word[i])
            # print(word[i], end="")
    nans = ''
    for k in ans:
        nans = nans+''+k
    return nans



if __name__ == "__main__":
    main()