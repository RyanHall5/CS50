import requests
import sys
import string

def main():
    #command line argument check
    if len(sys.argv) !=2:
        print("Invalid number of command-line arugments")
        sys.exit(1)


    #arugment number check
    if sys.argv[1].isdigit==False:
        print("command line argument is not a number")
        sys.exit(2)

    #converting to float
    num_bitcoin = float(sys.argv[1])



    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #storing response
    o = response.json()

    #getting bitcoin value from o
    price = o["bpi"]["USD"]["rate_float"]
    print(f"${price * num_bitcoin:,.4f}")
























main()