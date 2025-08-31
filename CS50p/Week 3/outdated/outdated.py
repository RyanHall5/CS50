import string
import sys

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():


    d,m,y = get_date("Date: ")
    print(f"{y}-{m:02}-{d:02}")


def get_date(prompt):

    while True:
        date = input(prompt).strip().title()
        if date[0].isnumeric():
            try:
                m,d,y = date.split("/")
                d,m,y=int(d),int(m),int(y)
                if m <= 12 and d<=31:
                    break
            except ValueError:
                pass
        else:
            try:
                m,d,y = date.split(" ")
                if d[len(d)-1]==",":
                    d,y=int(d[:-1]),int(y)
                    m = months.index(m)+1
                    if m <= 12 and d<=31:
                        break
            except ValueError:
                pass


    return d,m,y












main()