from jar import Jar


def test_init():
    jar = Jar().__init__()
    assert Jar().__init__() == jar


def test_str():
    jar = Jar(1)
    assert str(jar) == "🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(1)
    assert str(jar) == "🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar(1)
    jar.withdraw(1)
    assert str(jar) == ''