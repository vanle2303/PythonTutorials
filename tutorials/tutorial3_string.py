if __name__ == '__main__':
    str = "Hello World!"
    print(str)
    print(str[0])

    # Slicing : get chars in a specific range, not included the latter index. Eg. str[2:5]: We're abt to get the
    # chars from index 2 to index 4 and exclude index 5
    print(str[2:5])

    # Slice from the start
    print(str[:6])

    # Slice to the end
    print(str[2:])

    # Negative indexing means we start slicing from the end of the string, the last element has index of -1
    print(str[-5:-2])

    # * is the repetition operator
    print(str * 2)

    # + is the concatenation operator to concatenate (noi lien) the string
    print(str + "Test")

    s = "0123456789"
    s = s + " Hello!"
    print(s)    # 0123456789 Hello! ->> Concatenate 2 strings
    print("length of x: ", len(s))  # length of x:  17, need to call funct len(),no built-in function from string itself
    print(s.lower())    # 0123456789 hello!
    print(s.upper())    # 0123456789 HELLO!
    print(s.startswith("123"))  # False
    print(s.startswith("0"))    # True
    print(s.find("123"))    # 1 ->> return the lowest index where the substring is found
    print(s.rfind("123"))   # 1 ->> return the highest index where the substring is found
    print(s.find("Hello"))  # 11 ->> find() and rfind() return -1 on failure
    print(s.rfind("Hello"))  # 11
    print(s.count("123"))   # 1 ->> count the number of occurrences
    print(s.isdigit())  # False ->> isdigit() is a boolean func to test whether a string is a digit string or not
    #                     Digit String is a string that all its chars are digit(con so) and a digit string must contain
    #                     at least one char
    print(s.isnumeric())  # False ->> boolean func.
    #                       Numeric string is a string that all its chars are numeric and the string must contain
    #                       at least one char
    print(s.split())    # ['0123456789', 'Hello!']
    #                     split() is to split the string into a list of subs separated by space chars

    s1 = "123456123"
    s1 = s1.strip("123")    # strip(x) is to remove chars from both 2 ends and return the remaining chars
    print(s1)   # 456

    # Raw string. Use r or R right before the opening quote of the string to indicate that the input string is raw
    # and everything in the string will be printed out, including special characters like \n
    print("Hello \nIt's Van")   # Hello
    #                             It's Van  ->> This is a normal string and \n is treated as a sign to a new line
    print(r"Hello \n It's Van")  # Hello \n It's Van ->> This is a raw string, therefore, everything of the string will
    #                              be shown
    print(R"Hello \n It's me")  # Hello \n It's me  ->> Both r and R are the same

    s = "0123456789"
    print("0" in s)     # True
    print("0" not in s)     # False
    print("234" in s)   # True

    # Formatting string
    # The % sign is needed to separate the formatting string and the arguments
    print("My name is %s and weight is %d kg" % ("Van", 54))    # My name is Van and weight is 54 kg

    # Use format function. Note: Use named placeholder for better clarification
    s = "My name is {name} and my age is {age}".format(name="Van", age=19)  # My name is Van and my age is 19
    print(s)
    # or we can use format without names like this
    s = "My name is {} and my age is {}".format("Van", 19)
    print(s)    # My name is Van and my age is 19
    # or we can use number like this
    s = "My name is {0} and my age is {1}".format("Van", 19)
    print(s)    # My name is Van and my age is 19





