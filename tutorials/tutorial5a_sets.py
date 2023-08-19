if __name__ == '__main__':
    """
    set uses braces {} like dictionary 
    NOTE: 
        1. () tuple: immutable
        2. [] list: dynamic
        3. {} dict/set
    
    A set can store elements of different types but duplicated elements are ignored
    set CANNOT be accessed by index like in Java
    sets are mutable that they CAN be changed after created
    
    set in Python has s same feature like in Java, that is set cannot save the insertion order. Therefore, we cannot 
    rely on the inserted position. And each time running the prog, we may get different order of the elements in the set.
    That is bc each time of running, Python/Java use different cach thuc like creating different initial arrays
    """

    set1 = {"apple", "banana", 100}
    print(set1)         # {'banana', 100, 'apple'}  or {'apple', 100, 'banana'} or etc.
    print(type(set1))   # <class 'set'>
    print(len(set1))    # 3

    # Constructor using double parens
    set2 = set(("apple", "banana", "peach"))
    print(set2)         # {'apple', 'banana', 'peach'}  or  {'apple', 'peach', 'banana'} or so on

    x = set1.pop()  # remove and return an arbitrary element
    print(set1)     # {100, 'banana'}

    set1.update(set2)   # update() is to update a set with the union of itself and other
    print(set1)         # {'banana', 100, 'peach', 'apple'}

    set1.remove("peach")    # remove "peach". "peach" must be the member of set1, otherwise errors raised
    print(set1)             # {'apple', 100, 'banana'}

    set1.discard("melon")   # to remove an element from a set if it's a member; if not, do nothing. Better than remove()

    diff = set1.difference(set2)    # return the difference of 2 sets, the ones that in set1 but not in set2
    print(diff)     # {100}

    print(set1)     # {'banana', 100, 'apple'}
    print(set2)     # {'banana', 'peach', 'apple'}
    set1.difference_update(set2)    # to remove the elements of the other set in this set
    print(set1)     # {100}

    # added back to set1
    set1.add("apple")
    set1.add("banana")
    print(set1)     # {100, 'apple', 'banana'}

    x = set1.intersection(set2)     # return the intersection of two sets as a new set (elements present in both sets)
    print(x)    # {'banana', 'apple'}

    set1.intersection_update(set2)  # same as intersection() but the result will be stored in set1
    print(set1)     # {'apple', 'banana'}
    # added back to set1
    set1.add(100)

    print(set1.isdisjoint(set2))    # to check if the intersection is empty or not ->> False

    print(set1.issubset(set2))      # to check whether other set contains this set ->> False
    print(set1.issuperset(("apple", "banana")))    # to check if set1 is the superset of the input set ->> True

    sym_diff = set1.symmetric_difference(set2)  # return the symmetric difference of 2 sets ~ the elements are in
    #                                           either set1 or set2, but not in both
    print(sym_diff)     # {100, 'peach'}

    set1.symmetric_difference_update(set2)  # update the set by just keeping the symmetric difference of 2 set and store
    print(set1)     # {100, 'peach'}
    # remove and add back to get the original set1
    set1.discard("peach")
    set1.add("apple")
    set1.add("banana")
    print(set1)     # {100, 'apple', 'banana'}





