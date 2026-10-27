from bank import value

def test_start_with_h():
    assert value('Hey there') == '$20'

def test_start_with_hello():
    assert value('Hello, how you doing?') == '$0'

def  test_anything_else():
    assert value('What\'s up?') == '$100'