def main():
    text = input()
    newtext = convert(text)
    print(newtext)

def convert(text):
    newtext = text.replace(":)","🙂")
    newtext = newtext.replace(":(","🙁")
    return newtext

main()