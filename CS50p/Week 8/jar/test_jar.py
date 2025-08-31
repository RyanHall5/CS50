from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(5)
    assert jar2.capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(4)
    assert jar.size == 6

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    jar.withdraw(5)
    assert jar.size == 2