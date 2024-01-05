import re
import sys


def main():
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    print(convert(input("Hours: ")))



def convert(s):
    matches = re.search(r"^(([0-9][0-2]?):?([0-5][0-9])?) ([A|P]M) to (([0-9][0-2]?):?([0-5][0-9])?) ([A|P]M)$",s)
    if matches:
        mygroups = list(matches.groups())
        # print(mygroups)
        if (int(mygroups[1]) > 12 and mygroups[5] > 12):
            raise ValueError
        in_time = new_timing(mygroups[1],mygroups[2],mygroups[3])
        out_time = new_timing(mygroups[5],mygroups[6],mygroups[7])
        return in_time +' to '+out_time
        # return(mygroups)

    else:
        raise ValueError


def new_timing(hr,mini,meridium):
    if meridium == "PM":
        if int(hr) == 12:
            new_hr = 12
        else:
            new_hr = int(hr) + 12
    else:
        if int(hr) == 12:
            new_hr = 0
        else:
            new_hr = int(hr)

    if mini == None:
        new_min = ':00'
        new_read = f"{new_hr:02}" + new_min
    else:
        new_read = f"{new_hr:02}" + ':' + mini
    return new_read








if __name__ == "__main__":
    main()
# if (0 < matches.group(1) < 13 and (matches.group(2)==None or matches.group(2)=="00")):
            # if (0 < matches.group(3) < 13 and (matches.group(4)==None or matches.group(4)=="00")):
                # print()
        # elif (0 < matches.group(1) < 13 and matches.group(2))


        # print(re.search(r"^([0-9])?([0-9])?:?([0-9])?([0-9])? (AM|PM) to ([0-9])?([0-9])?:?([0-9])?([0-9])? (AM|PM)$",s))