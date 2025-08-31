import string

def main():
    time = input("What time is it? ")
    #chaning to int
    ctime = convert(time)
    #main condition
    if 7 <= ctime <= 8:
        print("breakfast time")
    elif 12 <= ctime <= 13:
        print("lunch time")
    elif 18 <= ctime <= 19:
        print("dinner time")




def convert(time):
    hours, minutes = time.split(sep=":")
    hours = float(hours) + float(minutes)/60
    return hours


if __name__ == "__main__":
    main()