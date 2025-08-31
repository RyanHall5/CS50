import string
from math import fabs

def main():

    owed = 50
    print(f"Amount Due: {owed}")

    #loop of question
    while(owed>0):

        coin = int(input("Insert Coin: "))#assumed integer input
        #checking if a valid coin
        if valid(coin):
            owed -= coin

        #printing amount left
        if owed>0:
            print(f"Amount Due: {owed}")
        else:
            print(f"Change Owed: {int(fabs(owed))}")



def valid(n):
    return (n == 25 or n == 10 or n == 5 or n == 1)



if __name__ == "__main__":
    main()