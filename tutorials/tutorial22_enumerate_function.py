"""
    Enumerate is to deal with iterators and keep count of iterations.
    Or basically, we use enumerate() to get both index and value while looping through a collection
    The result is returned in a form of enumerating object. The obj can be used directly for loop or be converted into
    a list of tuples using list() function.

    Syntax:     enumerate(iterable, start=0)
        iterable: any obj that supports iteration
        start: index value from which the counter starts, default value = 0

"""

if __name__ == '__main__':
    "Demos enumerate function in general"
    routine = ["eat", "sleep", "repeat"]
    s = "geek"

    # Create enumerate object
    obj1 = enumerate(routine)
    obj2 = enumerate(s)

    print("Return type:", type(obj1))   # Return type: <class 'enumerate'>
    print(list(enumerate(routine)))     # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

    # Changing starting index from 0 to 2
    print(list(enumerate(s, 2)))        # [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

    "Demos enumerate function in loops"
    # Printing tuples in obj directly
    for element in enumerate(routine):
        print(element)      # (0, 'eat')    (1, 'sleep')    (2, 'repeat')

    # Changing index and printing separately
    for count, element in enumerate(routine, 100):
        print(count, element)   # 100 eat   101 sleep   102 repeat

    # Getting desired output from tuple
    for count, element in enumerate(routine):
        print(count)
        print(element)
        """
        result:     0
                    eat
                    1
                    sleep
                    2
                    repeat
        """

