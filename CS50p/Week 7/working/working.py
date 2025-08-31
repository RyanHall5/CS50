import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s=s.strip()


    if matches := re.search(r"([1-9][0-9]?):?([0-5][0-9])? (AM|PM) to ([1-9][0-9]?):?([0-5][0-9])? (AM|PM)",s):
        pass
    else:
        raise ValueError


    #making new variables
    group1 = matches.group(1)
    group2 = matches.group(2)
    group3 = matches.group(3)
    group4 = matches.group(4)
    group5 = matches.group(5)
    group6 = matches.group(6)


    #special cases
    if group1 == "12" and group3 == "AM":
        group1 = "0"
    if group1 == "12" and group3 == "PM":
        group3 = "AM"

    if group4 == "12" and group6 == "AM":
        group4 = "0"
    if group4 == "12" and group6 == "PM":
        group6 = "AM"


    #hour for start time
    if group3 == "AM":
        start = group1
    else:
        start = str(int(group1) + 12)
    #minutes for start time
    if group2==None or group2=="00":
        start = start + ":00"
    else:
        start = start + ":" + group2


    #hour for end time
    if group6 == "AM":
        end = group4
    else:
        end = str(int(group4) + 12)
    #minutes for end time
    if group5==None or group5=="00":
        end = end + ":00"
    else:
        end = end + ":" + group5


    #adding 0 if needed
    if int(group1)<10 and group3 == "AM":
        start = "0" + start
    if int(group4)<10 and group6 == "AM":
        end = "0" + end


    return start + " to " + end


if __name__ == "__main__":
    main()