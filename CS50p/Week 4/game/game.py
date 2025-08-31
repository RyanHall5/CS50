import string
import random
import cs50
def main():


    level = get_int("Level: ")
    guess = get_int("Guess: ")
    answer  = int(random.uniform(1, level))
    if guess<answer:
        print("Too small!")
    elif guess>answer:
        print("Too large!")
    else:
        print("Just right!")


def get_int(prompt):

    while True:
        text = input(prompt)
        try:
            n = int(text)
            if n < 1:
                pass
            else:
                break
        except ValueError:
            pass
    return n

main()