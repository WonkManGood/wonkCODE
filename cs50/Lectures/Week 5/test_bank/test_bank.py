from bank import value

def test_bank():
    assert value("Hello") == 100
    assert value("h") == 20
    assert value("H") == 20
    assert value("ey") == 0