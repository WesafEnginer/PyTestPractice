from src.calculate import add   
def test_add_positive_numbers():
    result = add(3, 5)
    assert result == 8

def test_add_negative_numbers():
    result = add(-3, -5)
    assert result == -8

def test_add_mixed_numbers():
    result = add(4, -7)
    assert result == -3