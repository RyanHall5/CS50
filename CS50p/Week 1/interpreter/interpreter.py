import string

def main():
    expression = input("Expression: ")

    #splitting expression
    x, y, z = expression.split(sep=" ")
    # changing to floats
    x, z = float(x) , float(z)
    #checking operator
    match y:
        case "+":
            print(x+z)
        case "-":
            print(x-z)
        case "*":
            print(x*z)
        case "/":
            print(x/z)








main()