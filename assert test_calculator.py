from calculator1 import square

def test_square():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(-4) == 12
    assert square(0) == 0
