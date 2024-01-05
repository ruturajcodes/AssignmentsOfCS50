from seasons import check_date
from datetime import date


def main():
    test_correct_ver()
    test_incorrect_ver()


def test_correct_ver():
    assert check_date("2019-02-03") == date.fromisoformat("2019-02-03")
    assert check_date("2012-02-03") == date.fromisoformat("2012-02-03")

def test_incorrect_ver():
    assert check_date("January 5, 2022") == "NA"
    assert check_date("20000-05-45") == "NA"



if __name__ == "__main__":
    main()