import string


def main():
    text = input("Input: ")
    newtext = no_vowels(text)
    print(f"Output: {newtext}")


def shorten(text):
    for c in text:
        if c=="A"or c=="a"or c=="E"or c=="e"or c=="I"or c=="i"or c=="O"or c=="o"or c=="U"or c=="u":
            text = text.replace(c, "")
    return text











if __name__ == "__main__":
    main()