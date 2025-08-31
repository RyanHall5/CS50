import sys
import string
import csv

def main():
    #checking for only 1 argument
    if len(sys.argv)!=2:
        print("Incorrect number of command-line arguments")
        sys.exit(1)


    #checking for python file
    if sys.argv[1][-3:]!=".py":
        print("Not a python file")
        sys.exit(1)


    #opening file if it exists
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


    #initializing number of lines to 0
    num_lines=0


    #for every line in the file
    for line in file:
        #removing white spaces
        line = line.strip()

        #add one to count if not a blank line or comment
        if line != "" and line[0] != "#":
            num_lines+=1


    #printing number of lines
    print(num_lines)






    file.close()




if __name__ == "__main__":
    main()
