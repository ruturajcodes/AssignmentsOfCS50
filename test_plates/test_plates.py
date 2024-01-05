from plates import is_valid

def test_2_letter_start():
    assert is_valid("LL") == True

def test_not_2_letter_start():
    assert is_valid("L1") == False

def test_max_6():
    assert is_valid("AYUSHI") == True

def test_not_max_6():
    assert is_valid("AYUSHII") == False

def test_min_2_letter_start():
    assert is_valid("L") == False

def test_num_in_middle():
    assert is_valid("AAA22A") == False

def test_num_not_in_middle():
    assert is_valid("AAA222") == True

def test_num_0_in_mid():
    assert is_valid("AAA020") == False

def test_punc():
    assert is_valid(" ,:") == False

def test_alpha_num():
    assert is_valid("50CS") == False

def test_not_alpha_num():
    assert is_valid("CS 50") == False