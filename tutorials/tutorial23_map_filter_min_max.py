"""
NOTE: Lambda IS a Function
"""


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    # Functions max() and min() return the max and min elements of a collection
    my_max = max(list1)
    my_min = min(list1)

    print(my_max, my_min)  # 5  1
    # In case each element of a collection cannot be obviously comparable to other elements, we need to provide a
    # func, which maps each element of the collection to a value that Python can compare
    # Assume, we have a list of tuples

    list_of_tuples = [(1, 2, 3), (3, 2, 1), (4, 5, 6)]

    # Now we want to return the tuple with the max/min sum of all its element. So we need to provide a func that returns
    # the sum of all the elements in each tuple
    def tuple_sum(t):
        return t[0]+t[1]+t[2]

    # Now we can pass this function as the second arg to the min/max function. They will use this function to compare
    # the elements (tuples) in the list
    # I often get confused when passing function A as an argument to function B
    # That is bc of the auto-complete in Python. When hitting enter, function A always goes with braces, which makes
    # me think that I have to pass some args to A
    # But actually I only need to pass the name of the function, A, and nothing more
    my_min_tuple = min(list_of_tuples, tuple_sum)
    print(my_min_tuple)

    # Pass lambda as a function here, it returns a map obj, therefore, we have to convert it to a list
    mapped_obj = map(lambda x: x*x, list1)
    print(mapped_obj)   # <map object at 0x10b580940>
    # need to convert to a list
    square_list = list(mapped_obj)
    print(square_list)  # [1, 4, 9, 16, 25]

    # filter: to filter a collection with specific condition
    filtered = filter(lambda x: x>2, list1)
    print(filtered)     # <filter object at 0x105ed6430>
    # Still have to convert back to a list
    filtered_list = list(filtered)
    print(filtered_list)        # [3, 4, 5]



