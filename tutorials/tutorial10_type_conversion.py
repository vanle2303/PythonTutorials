"""
To convert data between different Python data types, we simply use the type name as the function
Eg. a = int(3)
"""

if __name__ == '__main__':
    # Conversion to int
    a = int(3)
    b = int(9.9)
    c = int("33")
    print(a, b, c)  # 3, 9, 33

    # Conversion to float
    a = float(3)
    b = float(9.9)
    c = float("33")
    print(a, b, c)  # 3.0, 9.9, 33.0

    # Conversion to string
    a = str(3)
    b = str(9.9)
    c = str("33")
    print(a, b, c)  # 3, 9.9, 33

    # eval() TAKES A STRING and evaluates it as a Python statement
    # it works like a compiler which compiles a string of code into an executable code
    x = eval("print(5)")
    print(x)    # return None, since now x is treated like a statement

    x = eval("2+2") # now x is NOT a statement, it is now a VAR, we need to print out its value explicitly
    print(x)    # 4

    # eval("5+7-")  --> syntax error since the string is not a valid python code fragment

    print(complex(1, 2))    # (1+2j)

    # repr(x) is similar to toString in Java, which also converts an obj into a representable string
    d = {1: "one", 2: "two"}
    print(d)    # {1: 'one', 2: 'two'}
    s = repr(d)
    print(s)    # {1: 'one', 2: 'two'}

    print(tuple((1, 2, 3)))     # (1, 2, 3)     Notice parens for tuple
    print(list((1, 2, 3)))      # [1, 2, 3]     Notice square brackets for list
    # print(list(1, 2, 3))  --> Type error:list expects at most 1 arg, therefore, must use paren to enclose the elements
    x = dict(((1, "one"), (2, "two")))  # dict() accepts a sequence of tuples of size 2 as (key, val)
    print(x)    # {1: 'one', 2: 'two'}

    print(chr(98))      # `b` converts an int to a char
    print(ord("b"))     # 98  converts a single char into int





