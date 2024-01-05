import inflect
import sys
import operator
from datetime import date, timedelta



p = inflect.engine()

def main():

    dob = input("Date of Birth: ")

    date1 = check_date(dob)
    if date1 == "NA":
        sys.exit("Invalid date")

    date2 = date.today()


    time_diff = operator.__sub__(date2, date1)
    # print(time_diff.days)



    num_diff = (time_diff.days)*24*60
    print((p.number_to_words(num_diff, andword="")).capitalize(),"minutes")


    # time_duration = timedelta(days=time_diff)
    # print(time_diff.days, time_diff.years)
    # print(type(time_diff))
    # difference = time_diff.days


def check_date(d):
    try:
        if "-" in d[4] and "-" in d[7]:
            loc_obj = date.fromisoformat(d)
        else:
            return "NA"

    except ValueError:
        return "NA"
    return loc_obj




if __name__ == "__main__":
    main()