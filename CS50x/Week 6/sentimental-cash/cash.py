def main():
    cents = get_cents()

    quarters = calc_quarters(cents)
    cents -= quarters*25

    dimes = calc_dimes(cents)
    cents -= dimes*10

    nickles = calc_nickles(cents)
    cents -= nickles*5

    pennies = cents
    cents -= pennies*1

    coins = quarters + dimes + nickles + pennies

    print(coins)







def get_cents():
    cents = -1
    while cents<0:
        try:
            cents = int(float(input("Cents: "))*100)
        except ValueError:
            pass
    return cents

def calc_quarters(cents):
    quarters = int(cents / 25)
    return quarters
def calc_dimes(cents):
    dimes = int(cents / 10)
    return dimes
def calc_nickles(cents):
    nickles = int(cents / 5)
    return nickles


main()
