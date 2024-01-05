from twttr import shorten

def test_vowel():
    assert shorten("dadu") == "dd"

def test_cap_vow():
    assert shorten("MANAS") == "MNS"

def test_conso():
    assert shorten("zdhs") == "zdhs"

def test_cap():
    assert shorten("ZDHS") == "ZDHS"

def test_num():
     assert shorten("12") == "12"

def test_punc():
    assert shorten(":") == ":"