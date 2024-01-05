imonth = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    try:
        idate = input("Date: ")
        mydate = idate.split("/")
        mm = int(mydate[0])
        dd = int(mydate[1])
        yy = int(mydate[2])

    except:
        try:
            ndate = idate.split(" ")
            mm = (ndate[0])
            if mm not in imonth:
                continue

            for k in range(len(imonth)):
                if mm == imonth[k]:
                    mm = int((k+1))
                    break

            if "," in ndate[1]:
                dd = int(ndate[1].replace(",",""))
            else:
                continue
            yy = int(ndate[2])

        except:
            pass

    if 1<=mm<=12 and 1<=dd<=31:
        print(f"{yy}-{mm:02}-{dd:02}")
        break
    else:
        continue
