from numb3rs import validate

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("256.2.3.4") == False
    assert validate("256.256.256.256") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.256") == False