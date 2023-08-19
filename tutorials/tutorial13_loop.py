"""
Loop types:
    1, while
    2, for
    3, nested loops: which contains a for loop inside another for loop, for example
Loop control statements:
    1, break
    2, continue   ->> break and continue work exactly the same as in Java
    3, pass: used when a statement is required syntactically but we don't want that peace of code to be executed

"""

if __name__ == '__main__':
    """
    while expression:
        statements
    """
    i = 0
    while i < 10:
        print(i)
        i += 1  # There is NO ++ in Python

    print()

    # while else
    i = 1
    while i < 3:
        print(i, end=", ")
        i += 1
    else:
        print("now i >= 3")
        print("indeed, i = ", i)

    i = 1
    while i != 1: print("i is not 1")   # if the body have only one line, we can write like this

    """ for loop syntax:
    for iterating_var in sequence:
        statements
    """
    fruits = ["banana", "apple", "melon"]
    for fruit in fruits:
        print(fruit)

    # use index
    for index in range(len(fruits)):
        print("fruit at index ", index, " is ", fruits[index])

    print()

    # for-else
    for fruit in fruits:
        print(fruit, end=", ")
    else:
        print()
        print("No more fruits")

    # break and continue
    for i in range(10):
        if i == 4: break
        if i % 2 == 0: continue
        print(i, end=", ")  # 1, 3,

    # pass statement
    """
    pass is used as a placeholder for future code.
    When pass is executed, nothing happens, but you can avoid getting a error where empty code is provided
    For example, empty code is not allowed in the following piece of code
    
    Also, notice that pass is used to make sth similar to interface in Java, meaning when we define a func, we can just 
    put pass to our code and no implementation yet. See func print() for example
    """
    for i in range(10):
        pass    # future code will be added here, with pass, no errors occur due to empty code



