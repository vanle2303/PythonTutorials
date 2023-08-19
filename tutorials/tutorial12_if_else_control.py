"""
Decision-making is if-else statements, which is also called control statement in Java
It also works the same way as in Java, we have 3 types:
    1, if
    2, if-else
    3, if-else if (nested if statements)

"""

if __name__ == '__main__':
    a = 100
    if a == 100:
        print("Value of expression is 100")
    else:
        print("Not 100")

    if a:   # since a = 100 != 0, null, it's True
        print(a)

    if a == 2:
        print("two")
    elif a == 0:    # This is else if, but written in short elif
        print("zero")
    else:
        print("Not 2 and 0")

    if a == 100: print(a)   # If there is only one statement inside if, the if block can go on the same line




