def main():
    plate = input("Plate: ")
    response = is_valid(plate)


    if response == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check length
    if len(s)<2 or len(s)>6:
        return False

    # 1st two characters should be letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False


    for j in s:
        if j.isdigit():
            index = s.index(j)
            if s[index:].isdigit() and int(j) != 0:
                return True
            else:
                return False




    # check for non inclusion of symbols, punctuations
    # for c in s:
    #     if c in ['!','@','#','$','%','^','&','*','(',')','_','+','-','~','`','/']:
    #         return False



    return True

if __name__ == "__main__":
    main()