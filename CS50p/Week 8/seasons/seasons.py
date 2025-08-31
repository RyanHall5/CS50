from datetime import date
import inflect
import sys

def main():
    inputDate = input("Date of Birth: ")
    print(convert(inputDate))

def convert(Date):
    today  = date.today()
    p = inflect.engine()
    try:
        y,m,d = Date.split("-")
        birth_date = date(int(y),int(m),int(d))
    except ValueError:
        sys.exit("Invalid Date")

    days_as_date = str(today-birth_date)
    end = days_as_date.index(" ")
    days = int(days_as_date[:end])
    minutes = days*24*60

    output = p.number_to_words(minutes).replace(" and","")
    output = output[0].upper() + output[1:]

    return output + " minutes"




if __name__ == "__main__":
    main()