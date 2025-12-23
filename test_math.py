#Math tests - practicing file creation

def test_addtion():
    result = 5 + 3
    assert result == 8

def test_subtraction():
    result = 10 - 4
    assert result == 6

def test_multi():
    result = 6 * 7
    expected = 42
    assert result == expected, f"Math failed: {result} != {expected}"

def test_division():
    result = 15/3
    assert result == 5