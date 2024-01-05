from um import count

def main():
    test_correct()
    test_correct_upper()
    test_incorrect()
    test_sep_by_space()


def test_correct():
    assert count('um') == 1

def test_correct_upper():
    assert count('Um, thanks, Um...,') == 2

def test_incorrect():
    assert count('umbrella') == 0
    assert count('yummy') == 0

def test_sep_by_space():
    assert count(' Um mango um') == 2

if __name__ == "__main__":
    main()