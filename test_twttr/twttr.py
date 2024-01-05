

def main():
    word = input("")
    # ans = []
    main_ans = shorten(word)

    print(main_ans,end="")
def shorten(word):
    ans = []
    vow = ["a","A","e","E","i","I","o","O","u","U"]

    for i in range(len(word)):
        if word[i] in vow :
            continue
        # elif word[i] in punc :
        #     continue
        # elif word[i] in ["1","2","3","4","5","6","7","8","9","0"]:
        #     # int(word[i])
        #     # if word[i] in numb:
        #         continue
        else:
            ans.insert(i,word[i])
            # print(word[i], end="")
    nans = ''
    for k in ans:
        nans = nans+''+k
    # if nans == "":
    #     return None
    return nans



if __name__ == "__main__":
    main()