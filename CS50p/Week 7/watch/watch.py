import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if "<iframe" not in s:
        return None

    if matches := re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)", s):
        return "https://youtu.be/" + matches.group(1)






if __name__ == "__main__":
    main()