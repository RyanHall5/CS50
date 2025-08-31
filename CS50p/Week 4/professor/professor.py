import random


def main():

    level = get_level()
    score = 0
    for i in range(10):
        count=0
        x = generate_integer(level)
        y = generate_integer(level)
        answer = str(x+y)
        user_answer = input(f"{x} + {y} = ").strip()
        while answer!=user_answer:
            count+=1
            if count==3:
                print(answer)
                break
            else:
                print("EEE")
            user_answer = input(f"{x} + {y} = ")
        if count != 3:
            score+=1
    print(f"Score: {score}")


#getting level from 1-3
def get_level():
    while True:
        s = input("Level: ")
        try:
            n = int(s)
            if 1<=n<=3:
                return n
        except ValueError:
            pass




#generate one random number with n digits
def generate_integer(level):
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)





if __name__ == "__main__":
    main()
