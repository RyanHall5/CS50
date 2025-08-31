from pyfiglet import Figlet
import sys
import random
import string
#figlet variables
figlet = Figlet()
fonts_list = figlet.getFonts()


def main():

    #command line argument check
    arguments=len(sys.argv)-1
    if (arguments!=0) and (arguments!=2):
        print("Invalid number of arguments")
        sys.exit(1)
    #making sure input is correct
    if arguments==2 and (sys.argv[1]!="-f" and sys.argv[1]!="--font"):
        print("Invalid argument 1")
        sys.exit(2)
    #making sure input is correct
    if arguments==2 and (sys.argv[2] not in fonts_list):
        print("Invalid argument 2")
        sys.exit(3)




    text = input("Input: ")
    if arguments == 0:
        rand_font = fonts_list[int(random.uniform(0,len(fonts_list)-1))]
        figlet.setFont(font=rand_font)
        print(figlet.renderText(text))
    else:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))







main()