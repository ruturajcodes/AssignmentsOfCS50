from numb3rs import validate

def test_oor():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False


def test_ir():
    assert validate(r"251.252.250.255") == True

def test_for_words():
    assert validate(r"cat.dog") == False

def test_first():
    assert validate(r"255.256.256.256") == False

def test_5bit_ip():
    assert validate(r"555.255.256.256.256") == False
