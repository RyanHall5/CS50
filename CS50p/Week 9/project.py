from runner import Runner
import sys
import csv
import operator

#global variable to make things simpler in main
runners_lists = {"all":{"all":[],"9":[],"10":[],"11":[],"12":[]},
                 "m":{"all":[],"9":[],"10":[],"11":[],"12":[]},
                 "f":{"all":[],"9":[],"10":[],"11":[],"12":[]}}

#trying to keep main very readble so there will be a lot of functions to avoid clutter
def main():

    #checking command-line arguments
    valid_commands()

    #opening File handler
    file = open_establish_file()

    #reading and organizing data from file into dict
    read_data(file)


    #sort all of the runners
    for gen_list in runners_lists.values():
        for grade_list in gen_list.values():
            grade_list.sort(key=operator.attrgetter('pr_seconds'))


    #main function for user choosing what to see
    while True:
        choice = valid_choice()
        match choice:
            case 1:
                gen_sort, grade_sort = get_specifications()
                n = get_num()
                print_top(n,gen_sort,grade_sort)
            case 2:
                gen_sort, grade_sort = get_specifications()
                rank = get_rank()
                runner = get_runner(rank,gen_sort,grade_sort)
                print(f"\n{runner}\n")
            case 3:
                runner = get_name()
                print(f"\n{runner}\n")
            case 4:
                sys.exit("\n\nProgram Exited")
            case _:
                pass


def get_num():
    num = None
    while not (isinstance(num, int) and num>0):
        try:
            num = int(input("How many runners: "))
        except ValueError:
            pass
    return num


def print_top(n,gen,grade):
    print("")
    try:
        for i in range(n):
            print(runners_lists[gen][grade][i])
    except IndexError:
        pass
    print("")


def get_runner(rank,gen,grade):
    try:
        runner = runners_lists[gen][grade][rank-1]
    except IndexError:
        runner = "No Runner exists at that rank"
    return runner


def get_rank():
    num = None
    while not (isinstance(num, int) and num>0):
        try:
            num = int(input("Rank: "))
        except ValueError:
            pass
    return num

def get_name():
    while True:
        n = input("Name: ").lower().strip()
        for runner in runners_lists["all"]["all"]:
            if runner.name == n:
                return runner

def get_specifications():
    gender_choice = None
    while gender_choice not in ["all","m","f"]:
        gender_choice = input("What gender would you like to sort by?(all,m,f)")

    grade_choice = None
    while grade_choice not in ["9","10","11","12", "all"]:
        grade_choice = input("What grade would you like to sort by?(all,9,10,11,12)")

    return gender_choice, grade_choice


def valid_choice():
    choice = None
    while choice not in [1,2,3,4]:
        try:
            choice = int(input("Chose an Option by typing the choice number:\n1. See top _ runners in a category\n2. See what runner is at a specific rank\n3. See the stats for a specific runner\n4. Exit\n"))
        except ValueError:
            pass
    return choice

def read_data(file):

    #reading in every runner and adding them to appropriate lists
    for line in file:
        name,pr,grade,gender = line["name"].lower(),line["pr"],line["grade"],line["gender"]
        runners_lists["all"]["all"].append(Runner(name,pr,grade,gender))
        runners_lists["all"][grade].append(Runner(name,pr,grade,gender))
        runners_lists[gender]["all"].append(Runner(name,pr,grade,gender))
        runners_lists[gender][grade].append(Runner(name,pr,grade,gender))


def open_establish_file():
    #opening file if it exists
    try:
        in_file = open(sys.argv[1])
    except FileNotFoundError:
        raise ValueError("File does not exist")

    #establishing file handler
    return csv.DictReader(in_file)


def valid_commands():
    #check ammount of arugments
    if len(sys.argv)!=2:
        raise ValueError("Incorrect number of command-line arugments")

    #check for correct file type
    if sys.argv[1][-4:]!=".csv":
        raise ValueError("File is not a csv file")




if __name__ == "__main__":
    main()