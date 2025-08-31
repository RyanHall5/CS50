from plates import is_valid

def test_is_valid():
    assert is_valid("nope") == True
    assert is_valid("thisistoolong123") == False
    assert is_valid("numb3r") == False
    assert is_valid("zer02") == False
    assert is_valid("lol.12") == False
    assert is_valid("12") == False
