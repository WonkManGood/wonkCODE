from plates import is_valid

def test_alpha_start():
    assert is_valid("ASS") == True
    assert is_valid("4ASS") == False
    assert is_valid("GK50") == True
    assert is_valid("G6R3") == False

def test_length_check():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("WAWAWAK") == False

def test_beginsalpha():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("5") == False
    assert is_valid("C0") == False

def test_num_placement():
    assert is_valid("AAA111") == True
    assert is_valid("AA11AA") == False
    assert is_valid("AAA22A") == False

def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("0CS50") == False
    assert is_valid("CS050") == False

def test_alnum_check():
    assert is_valid("???") == False
    assert is_valid("FUCKTHISMAN!") == False
    assert is_valid("MINE.") == False