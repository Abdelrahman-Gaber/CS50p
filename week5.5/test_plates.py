from plates import is_valid

def test_not_starting_with_2_chars():
    assert is_valid('5434') == False

def test_starting_with_2_chars():
    assert is_valid('CS50') == True

def test_number_starts_with_0():
    assert is_valid('CS050') == False

def test_less_than_2_chars():
    assert is_valid('C') == False

def test_more_than_6_chars():
    assert is_valid('CS54321') == False