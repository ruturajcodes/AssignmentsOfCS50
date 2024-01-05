import sys
import csv

def main():
    check_file()
    table1 = []
    try:
        with open(sys.argv[1],"r") as file1:
            reader = csv.DictReader(file1)
            file2 = open(sys.argv[2],"w",newline="")

            fieldnames = ['first','last','house']
            writer = csv.DictWriter(file2, fieldnames=fieldnames)

            writer.writerow({"first":"first", "last":"last", "house":"house"})
            for row in reader:
                name = row["name"].split(",")
                for i in range(len(name)):
                    # lname = ""
                    # fname = ""
                    if i == 0:
                        lname = name[i]
                        # print("lname:",lname)
                    elif i == 1:
                        fname = name[i].lstrip()
                        # print("fname:",fname)
                # naaam = fname+" "+lname
                # print(naaam)
                # table1.append(name[1])
                # det = [fname,lname,row["house"]]
                ghar = row["house"]
                # table1.append(det)
                writer.writerow({"first":fname, "last":lname, "house":ghar})
            # print(table1)



            # print(table1)
            file2.close
            # with open(sys.argv[2],"w",newline="") as file2:
            #     writer = csv.writer(file2)
            #     for row in reader:
            #         writer.writerows(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def check_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()