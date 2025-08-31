import string
import sys
from PIL import Image , ImageOps


if len(sys.argv)!=3:
    print("Incorrect number of command-line arguments")
    sys.exit(5)

#checking for image file
if sys.argv[1][-4:]!=".jpg" and sys.argv[1][-5:]!=".jpeg" and sys.argv[1][-4:]!=".png":
    print("First file is not a csv file")
    sys.exit(2)


#checking for csv file
if sys.argv[2][-4:]!=".jpg" and sys.argv[2][-5:]!=".jpeg" and sys.argv[2][-4:]!=".png":
    print("Second file is not a csv file")
    sys.exit(2)


#checking if files have same extension
period1 = sys.argv[1].find(".")
period2 = sys.argv[2].find(".")
if sys.argv[1][period1:]!=sys.argv[2][period2:]:
    print("file types do not match")
    sys.exit(3)


try:
    file = Image.open(sys.argv[1])
except FileNotFoundError:
    print("file does not exist")
    sys.exit(4)

shirtfile = Image.open("shirt.png")

size = shirtfile.size

muppet = ImageOps.fit(file, size)

muppet.paste(shirtfile, shirtfile)

muppet.save(sys.argv[2])






