height = 0
while height<1 or height>8:
    try:
        height = int(input("Height: "))
    except ValueError:
        pass

i = 1
while i<=height:
    j=height
    while j>0:
        if j>i:
            print(" ", end="")
        else:
            print("#", end="")
        j-=1
    print("  ", end="")

    k = 0
    while k<height:
        if k<i:
            print("#", end="")
        k+=1
    print("\n", end="")
    i+=1


