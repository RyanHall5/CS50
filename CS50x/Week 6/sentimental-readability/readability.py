def main():

    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentances = count_sentances(text)

    L = float(letters)/words*100
    S = float(sentances)/words*100

    grade = round(.0588 * L - .296 * S -15.8)

    if grade<1:
        print("Before Grade 1")
    elif grade>=16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def count_letters(text):
    letters = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters+=1
    return letters

def count_words(text):
    words = 0
    for i in range(len(text)):
        try:
            if (text[i]!=" " and text[i+1] == " "):
                words+=1
        except IndexError:
            if (text[i]!= " " and i==len(text)-1):
                words+=1
    return words

def count_sentances(text):
    sentances = 0
    for i in range(len(text)):
        if text[i]=="!" or text[i]=="." or text[i]=="?":
            sentances+=1
    return sentances

main()
