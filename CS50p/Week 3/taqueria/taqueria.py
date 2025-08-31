import string

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

def main():

    total=0.0
    while True:
        item = get_item("Item: ").title()
        if item=="Stop":
            print()
            break
        if valid(item):
            total+= menu[item]
            print(f"Total: ${total:.2f}")




def valid(s):
    while True:
        try:
            price = menu[s]
            return True
        except KeyError:
            return False

def get_item(prompt):
    try:
        item = input(prompt)
        return item
    except EOFError:
        return "Stop"



main()