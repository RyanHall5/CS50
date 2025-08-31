import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py FILENAME TEXTNAME")
    # TODO: Read database file into a variable
    file1 = open(sys.argv[1])
    csv_file = csv.DictReader(file1)

    database = []
    for person in csv_file:
        database.append(person)

    # TODO: Read DNA sequence file into a variable
    file2 = open(sys.argv[2])
    txt_file = csv.reader(file2)
    for line in txt_file:
        sequence = str(line).replace("[","").replace("'","").replace("]","")

    # TODO: Find longest match of each STR in DNA sequence
    longest_matches = []
    STRs = list(database[0].keys())
    STRs.remove("name")
    for sub in STRs:
        longest_matches.append(longest_match(sequence, sub))

    # TODO: Check database for matching profiles
    for i in range(len(database)):
        count = 0
        for j in range(len(STRs)):
            if database[i][STRs[j]] == str(longest_matches[j]):
                count+=1
            if count == len(STRs):
                print(database[i]["name"])
                break
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
