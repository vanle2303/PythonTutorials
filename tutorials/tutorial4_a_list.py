"""
Basically list is pretty much the same as in Java
list is a dynamic array
List is declared by using []

Note:
    1. () tuple: immutable
    2. [] list: dynamic
    3. {} dict/set
"""

if __name__ == '__main__':
    list = ['abcd', 123, 4.56, "Van", 333]
    sub_list = [123, "Van"]
    print(list)             # ['abcd', 123, 4.56, 'Van', 333]
    print(list[0])          # abcd
    print(sub_list * 2)     # [123, 'Van', 123, 'Van']
    print(list + sub_list)  # ['abcd', 123, 4.56, 'Van', 333, 123, 'Van']
    list.append("Long")
    print(list)             # ['abcd', 123, 4.56, 'Van', 333, 'Long']

    list1 = [1, 2, 3, "four"]
    list2 = ["five", 6]
    print(type(list1))  # <class 'list'>
    print(list1)
    print(list1+list2)  # [1, 2, 3, 'four', 'five', 6]
    print(len(list1))   # 4
    print(list1[3])     # four ->> accessing elements like in arrays
    print(list1[1:3])   # [2, 3] ->> sublist from the element at index 1 to index 2, excluding index 3
    print(list1[1:])    # [2, 3, 'four'] ->> sublist from index 1 to the end of the list
    list3 = list1*2
    print(list3)        # [1, 2, 3, 'four', 1, 2, 3, 'four']
    print(list3.count("four"))  # 2  ->> count the number of occurrences
    list1.reverse()     # reverse list1
    print(list1)    # ['four', 3, 2, 1]
    list1.reverse()     # now reverse list1 back to its original order
    print(list1.pop(3))     # `four`  ->> remove and return the element at a specific index
    print(list1)    # [1, 2, 3]
    list1.append("four")    # add "four" back to the end of the list
    print(list1)    # [1, 2, 3, 'four']
    list1.remove("four")
    print(list1)    # remove the very first occurrence of given element in the list
    list1.append("four")
    print(list1.index("four"))  # 3
    list1.append(list2)  # add the whole list2 as the last element of list1 (nested list)
    #                      It's different from print(list1+list2), which just appends the elements of list2 into list1
    print(list1)    # [1, 2, 3, 'four', ['five', 6]]
    list1.insert(0, "five")     # insert an ibj at the given index
    print(list1)    # ['five', 1, 2, 3, 'four', ['five', 6]]
    list1.clear()   # clear list1 and now list1 is empty
    print(list1)

    # sorting
    list4 = [(4, "four"), (2, "two"), (5, "five"), (3, "three")]    # a list of tuples that we wanna sort

    def get_key(t):
        return t[0]
    list4.sort()
    print(list4)    # [(2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
    list4.sort(key=get_key)  # pass func get_key to built-in func sort
    print(list4)    # [(2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
    list4.sort(key=get_key, reverse=True)
    print(list4)    # [(5, 'five'), (4, 'four'), (3, 'three'), (2, 'two')]

    list5 = [1, 5, 3, 4, 2, 6]
    list5.sort()
    print(list5)    # [1, 2, 3, 4, 5, 6]

    #  A list of tuples, each tuple describes a person (name, age, salary)
    list_of_people = [("Long", 12, 20000), ("John", 5, 100000), ("Van", 19, 50000)]
    list_of_people.sort()
    print(list_of_people)   # [('John', 5, 100000), ('Long', 12, 20000), ('Van', 19, 50000)]

    # These steps are to sort people based on their salary
    # This func takes params of tuples and returns the tuple's element at specific index
    def get_salary(t):
        return t[2]
    # We're using a list to call func sort(). And now we pass func get_salary to func sort()
    # This step is NOT to call func get_salary but now get_salary is treated like a value and passed to other funcs
    list_of_people.sort(key=get_salary)
    print(list_of_people)   # Sort by salary: [('Long', 12, 20000), ('Van', 19, 50000), ('John', 5, 100000)]

    # These steps are to sort people based on their ages
    def get_age(t):
        return t[1]
    list_of_people.sort(key=get_age)
    print(list_of_people)   # Sort by age: [('John', 5, 100000), ('Long', 12, 20000), ('Van', 19, 50000)]

    # LIST COMPREHENSION
    list6 = [1, 2, 3, 4]

    # This is to get the square of each element in a list and then return a new list of all squared elements
    list6 = [i*i for i in list6]
    print(list6)    # [1, 4, 9, 16]

    # This demos the operation of a list with more than 1 condition
    # Here, for each odd element, multiply it by 2
    list6 = [i*2 for i in list6 if i % 2 == 1]
    print(list6)    # [2, 18]




