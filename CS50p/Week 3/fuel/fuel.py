import string
import math
#errors ValueError ZeroDivisionError


def main():
    x, y = get_fraction("Fraction: ")
    percent = change_to_percent(x,y)
    print(percent)



def change_to_percent(x,y):
    try:
        percent = round(x/y *100)
    except: ZeroDivisionError
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return str(percent) + "%"





def get_fraction(prompt):
    while True:
        try:
            text = input(prompt)
            x, y = text.split(sep="/")
            x, y = int(x), int(y)
            if x <= y:
                return x, y
        except ValueError:
            pass


main()