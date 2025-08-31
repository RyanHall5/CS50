import string

def main():
    camelCase = input("camelCase: ")

    snakeCase = convert(camelCase)

    print(snakeCase)

def convert(camel):
    for i in range(len(camel)):
        if camel[i].isupper():
            camel = camel[:i] + "_" + camel[i:]
            change = camel[i+1]
            camel = camel.replace(change,change.lower())


    return camel




if __name__ == "__main__":
    main()