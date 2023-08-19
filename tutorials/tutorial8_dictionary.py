"""
Dict is kinda hash table type consisting of key-value pairs
Dict encloses by curly braces {} and values can be assigned and accessed by square braces []
Keys can be any types but usually string or number
Values can be any types

Note:
    When duplicate keys are encountered the last key assignment wins
    Keys must be immutable like string, numbers, tuples but cannot be list
"""

if __name__ == '__main__':
    dict0 = {}
    dict0['one'] = "This is one"
    dict0 [2] = "This is two"

    sub_dict0 = {'name': 'Van', 'id': 123, 'job': 'student'}

    print(dict0)         # {'one': 'This is one', 2: 'This is two'}
    print(sub_dict0)     # {'name': 'Van', 'id': 123, 'job': 'student'}
    print(dict0['one'])  # This is one
    print(sub_dict0.keys())  # dict_keys(['name', 'id', 'job'])
    print(sub_dict0.values())    # dict_values(['Van', 123, 'student'])

    dict1 = {0: "zero", "three": 3}  # keys can be of different types
    dict1[1] = "one"
    dict1[2] = "two"
    dict2 = {5: "five"}

    print(dict1)    # {0: 'zero', 'three': 3, 1: 'one', 2: 'two'}
    print(dict1[1]) # one, get value of key `1`

    key_set = dict1.keys()   # get the key set of dict1
    print(key_set)   # dict_keys([0, 'three', 1, 2])
    values_set = dict1.values() # get the values set of dict1
    print(values_set)   # dict_values(['zero', 3, 'one', 'two'])

    print(dict1.get(1)) # get value `one` from a given key
    print(dict1.get("apple"))   # get None since the key doesn't exist
    '''
    "The key doesn't exist" is a default val if key "apple" doesnt exist'''
    print(dict1.get("apple", "The key doesn't  exist"))

    print(dict1.pop(1)) # pop() is to get the value of a specific key and then delete that key-value pair
    print(dict1)    # dict1 after pop(): {0: 'zero', 'three': 3, 2: 'two'}
    dict1[1] = "one"    # add that pair back to dict1
    print(dict1)    # dict1 after adding that removed pair back: {0: 'zero', 'three': 3, 2: 'two', 1: 'one'}

    items = dict1.items()   # return a set of items
    print(items)    # dict_items([(0, 'zero'), ('three', 3), (2, 'two'), (1, 'one')])
    for item in items:
        '''
        `end=` is an arg of print statement, which is to print sth after the print statement is done
        Normally end= comes with a default value of `\n` that is auto move to the next line
        Therefore, if we wanna print sth else after that print statement or wanna print everything in one line
        we just need to customize the value of end= '''
        print(item, end=", ")
        print(type(item))   # <class 'tuple'>

    print(dict1.popitem())  # remove and return the LAST ADDED item to the dict like STACK in Java: (1, 'one')
    dict1[1] = "one"    # add it back

    # Check if a key is in a dict
    print(8 in dict1)   # False
    if 8 in dict1:  # NOTHING returned
        print("This wont execute")
    if 8 not in dict1:
        print("The key is not in the dict") # The key is not in the dict

    # This is similar to the get() to set default value for non-existing key
    print(dict1.setdefault(10, "ten"))  # ten, since key 10 is not in the key so it sets value "ten" to key 10
    print(dict1.get(10))    # now, 10 is in dict1
    print(dict1)    # {0: 'zero', 'three': 3, 2: 'two', 1: 'one', 10: 'ten'}

    # clear and delete a dict
    dict1.clear()   # clear all the content of dict1
    print(dict1)    # {}
    del dict1   # delete everything of dict1, so now dict1 no longer exists, not even {}
    # print(dict1)=> NameError, this statement is no longer available since dict1 doesn't exist
    dict1 = {0: 'zero', 'three': 3, 2: 'two'}   # create dict1 back

    # Dict Keys MUST be of IMMUTABLE types: string, tuple, number NOT list or set
    list1 = ['nine']
    # dict1[list1] = 9    # => TypeError: unhashable type: 'list', it's illegal to use a mutable val to assign to a key

    # Update a dict by adding new values from another dict
    # Now the old value "zero" of 0 will be replaced by the new value "ZERO"
    dict1.update({"apple": "Tim Cook", "tesla": "Elon Musk", 0: "ZERO"})
    print(dict1)    # {0: 'ZERO', 'three': 3, 2: 'two', 'apple': 'Tim Cook', 'tesla': 'Elon Musk'}

    apples = [k for k in dict1 if k == "apple"] # ['apple']
    print(apples)
    apples_value = [v for k, v in dict1.items() if k == "apple"]    # ['Tim Cook']
    print(apples_value)















