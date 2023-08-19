"""
Tuple is like List but READ-ONLY list
In other words, Tuple is immutable array, it is declared by using ()
Note:
    1. () tuple: immutable
    2. [] list: dynamic
    3. {} dict/set
"""

if __name__ == '__main__':
    tuple0 = ('abcd', 123, 4.56, "Van", 333)
    sub_tuple = (123, "Van")

    print(tuple0)
    print(tuple0[0])
    print(tuple0[1:3])  # result: (123, 4.56), include 1st exclude 3rd
    print(tuple0[2:])  # (4.56, 'Van', 333), include 2nd to the end of the tuple
    print(sub_tuple * 2) # (123, 'Van', 123, 'Van') repeat the sub-tuple twice
    print(tuple0 + sub_tuple)    # ('abcd', 123, 4.56, 'Van', 333, 123, 'Van')

    tuple1 = (1, 2, 3, 'four')
    tuple2 = ('five', 6)
    print(tuple1)
    print(tuple1 + tuple2)  # (1, 2, 3, 'four', 'five', 6)
    print(tuple1.index(3))  # 2, return a value at a specific index
    print(tuple1.count(1))  # 1, return the number of occurrences of a value
    print(len(tuple1))      # 4, return the length of the tuple

    # Convert a tuple into a list
    list1 = list(tuple1)
    print(list1)

    # Convert a list into a tuple
    t = tuple(list1)
    print(t)

    single_tuple = (1,)
    print(single_tuple)

    # Any sequences declared without parens (), brackets [] or braces {} are defaulted to be a tuple
    # Therefore, when declaring a tuple, it's optional use ()
    # However, when declaring a list, we MUST show the brackets []
    tuple3 = 1, 2, 3, 4, 5, 6
    print(tuple3)   # (1, 2, 3, 4, 5, 6)
    print(type(tuple3))     # <class 'tuple'>


