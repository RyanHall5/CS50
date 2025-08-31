import string


def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    str=greeting.lower().strip()
    if str.find("hello") == 0:
        return 0
    elif str.find("h") == 0:
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()
