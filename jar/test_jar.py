from jar import Jar


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(8)
    assert jar2.capacity == 8


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar()
    jar1.deposit(5)
    assert jar1.size == 5
    jar1.deposit(2)
    assert jar1.size == 7


def test_withdraw():
    jar1 = Jar()
    jar1.deposit(5)
    jar1.withdraw(2)
    assert jar1.size == 3
    jar1.withdraw(2)
    assert jar1.size == 1