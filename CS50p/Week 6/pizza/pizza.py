import string
import csv
import sys
from tabulate import tabulate

def main():
    #checking for only 1 argument
    if len(sys.argv)!=2:
        print("Incorrect number of command-line arguments")
        sys.exit(1)


    #checking for csv file
    if sys.argv[1][-4:]!=".csv":
        print("Not a csv file")
        sys.exit(1)

    #declaring list
    pizzas = []

    with open (sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for line in reader:
            pizzas.append(line)

    #printing
    print(tabulate(pizzas, headers = "keys", tablefmt="grid"))

    #print(pizzas)







if __name__ == "__main__":
    main()