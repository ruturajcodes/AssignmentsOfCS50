from bank import value

def test_hello():
    assert value("hello") == 0


def test_hstart():
    assert value("hii") == 20


def test_other():
    assert value("namaste") == 100

def test_caseins():
    assert value("HELLO") == 0
    assert value("HII") == 20
    assert value("NAMASTE") == 100