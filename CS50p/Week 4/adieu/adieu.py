import string

def main():
    names = []

    name = get_name("Name: ")
    #loop getting names
    while name!="EOFError":
        names.append(name)
        name = get_name("Name: ")
    print()
    print("Adieu, adieu", end="")
    for name in names:
        #if only one name or two names
        if len(names) == 1:
            print(f", to {name}", end="")
            break
        elif len(names) == 2:
            print(f", to {names[0]} and {names[1]}",end="")
            break
        #if more than one name
        if name == names[len(names)-1]:
            print(f", and {name}", end="")
        elif name == names[0]:
            print(f", to {name}", end="")
        else:
            print(f", {name}", end="")
    print()




def get_name(prompt):
    try:
        name = input(prompt)
        return name
    except EOFError:
        return "EOFError"

main()