import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #get a return value for each number in the ip adress and check if it is under 255
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)


    try:
        if int(matches.group(1))>255 or int(matches.group(2))>255 or int(matches.group(3))>255 or int(matches.group(4))>255:
            return False
    except AttributeError:
        return False

    return True



if __name__ == "__main__":
    main()