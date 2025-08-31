import string
import csv
import sys

def main():
    #checking for 2 arguments
    if len(sys.argv)!=3:
        print("Incorrect number of command-line arguments")
        sys.exit(1)

    #checking for csv file
    if sys.argv[1][-4:]!=".csv":
        print("First file is not a csv file")
        sys.exit(1)


    #checking for csv file
    if sys.argv[2][-4:]!=".csv":
        print("Second file is not a csv file")
        sys.exit(1)


    #opening file if it exists
    try:
        in_file = open(sys.argv[1])
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    students = []
    #reading file into list
    reader = csv.DictReader(in_file)
    for line in reader:
        students.append(line)

    #closing file
    in_file.close()


    #reorganizing data and sending it to other list
    new_students = []
    new_student = {}

    for student in students:
        last, first = student["name"].split(", ")
        house = student["house"]
        new_student = {"first":first, "last":last, "house":house}
        new_students.append(new_student)


    #opening second file passed in as writing file
    with open(sys.argv[2], "w") as out_file:
        #writing organized list of students to outfile
        writer = csv.DictWriter(out_file, fieldnames = ["first","last","house"])
        writer.writeheader()
        for student in new_students:
            writer.writerow({"first":student["first"], "last":student["last"], "house":student["house"]})









if __name__ == "__main__":
    main()