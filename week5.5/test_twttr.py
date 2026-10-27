from twttr  import shorten

def test_uppercase():
    assert shorten('TWITTER') == 'TWTTR'

def test_lowercase():
    assert shorten('twitter') == 'twttr'