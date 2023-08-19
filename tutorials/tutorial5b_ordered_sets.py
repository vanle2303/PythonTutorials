"""
Ordered sets works exactly like LinkedHashSet in Java

Failed to install ordered_set, we have to run this ( pip install ordered_set) in Terminal
Then "from ordered_set import OrderedSet" statement is legal
"""

from ordered_set import OrderedSet

if __name__ == '__main__':

    set1 = OrderedSet([2, 1, 4, 2, 9, 3])
    for x in set1:
        print(x, end=", ")  # 2, 1, 4, 9, 3, ->> Insertion order is saved
    print()

    set2 = set([2, 1, 4, 2, 9, 3])
    for i in set2:
        print(i, end=", ")  # 1, 2, 3, 4, 9,    ->> Random order
    print()

    # Dict in Python3 is ordered but in Python2, we have to use OrderedDict
    dict = {1: "one", 5: "five", 2: "two", 4: "four", 3: "three"}
    for i in dict.items():
        print(i, end=", ")
        print("type of i:", type(i))        # (1, 'one'), type of i: <class 'tuple'> and so on
