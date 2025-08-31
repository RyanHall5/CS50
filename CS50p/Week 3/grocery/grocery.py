import string

def main():

    grocery = {}


    while True:
        item = get_item().upper()
        #if control-d
        if item == "EOFERROR":
            break

        #adding 1 to item or adding item to list
        if item in grocery:
            grocery[item]+=1
        else:
            grocery[item]=1

    for item in sorted(grocery):
        print(grocery[item], item)





def get_item(prompt = ""):
    try:
        item = input(prompt)
        return item
    except EOFError:
        return "EOFError"

main()