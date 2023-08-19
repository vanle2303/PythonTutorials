"""
The syntax to define a function in Python:
    def func-name(params):
        "function doc-string"
        statements
All params in Python are passed by reference

There are 4 types of args in Python functions:
    1, Required args (no default values provided)
    2, Keyword arguments: specify the param name when calling the function
            eg: print_string(str="Hello")
    3, Default argument: If we don't provide any args to the function when calling it, it will use the default value provided
            eg: def my_info (name, age=19)
    4, Variable length argument: like in Java, we can pass as many args to the function as we desire
            eg: def get_num (*var_args_tuple)
"""

if __name__ == '__main__':
    # A basic demo of function
    def get_sum(a, b):  # This is to define a function
        return a + b
    # This is a call to the previously defined function
    print(get_sum(1, 2))

    # pass by reference
    def print_list(mylist):
        "This changes a passed list to this function"
        mylist.append([1, 2, 3, 4])
        print("My list after the change to reference is: ", mylist)
        return
    # A call to function pass_by_reference
    print_list([0])

    """
    Keywords arguments, that is when passing an arg to a func, we can use syntax param-name = arg
    """
    def print_string (str):
        print(str)
        return
    # Now we call print_string func with keyword call
    print_string(str="Hello")

    """
    This is another example of keyword argument with a special syntax: def func-name (pram-list1, *, param-list2)
    That is, when calling the func, params in param-list2 must be specified by keyword argument
    """
    def print_data (x, y, *, z, u, v):
        print(x, y, z, u, v)
        return
    # print_data(1, 2, 3, 4, 5)     ->> This is illegal
    print_data(1, 2, z=3, u=4, v=5)     # 1 2 3 4 5
    print_data(1, 2, v=5, u=4, z=3)     # 1 2 3 4 5

    # Default arguments
    def print_info (name, age=12):  # Now age is optional since it is set a default value of 12
        "This prints passed info to the function"
        print("Name: ", name)
        print("Age: ", age)
        return
    print_info("Van", 19)   # Name:  Van    Age:  19
    print_info("Long")      # Name:  Long   Age:  12

    # Variable length arguments
    """
    Syntax for variable length arguments:
        def func-name (normal-params, *var_args_tuple):
            "function_docstring"
            function_suite
            return [expression]
    """
    def print_num (arg1, *var_tuple):
        # arg1 is a required argument but var_tuple is optional. It can contain as many args as possible
        # or it can contain no args. Since the values are comma separated, they are treated as a tuple of values
        print("Output is: ")
        print(arg1)
        for var in var_tuple:
            print(var)
        return
    print_num(1)    # Output is: 1
    print_num(1, 2, 3)  # Output is: 1 2 3

    """
    Anonymous function, which works the same as lambda in Java
    Anonymous functions are not defined in a standard way using def, but it is defined with lambda keyword
    Syntax:
        lambda (param-list): expression 
    Lambda form can take any numbers of args, but return just one in the form of an expression
    It cannot contain any command or multiple expression
    Lambda functions have their own namespace, and cannot access vars other than those in their param list and in 
    the global namespace
    """
    # This is a function definition, sum is function name. Note: NO return word is needed, just like a short Java lambda
    sum = lambda x, y: x + y
    # Now we can call sum as a normal function
    print("sum =", sum(1, 2))   # sum = 3

    """
    In Java, in order to return more than 1 field, we encapsulate them into an object and then return the fields of that
    obj
    However, in Python, we can just return multiple fields within return statement
    Then all the fields returned will be automatically encapsulated in a tuple, and the result will be a tuple of fields
    """
    def sum_and_sub (x, y):
        sum = x + y
        sub = x - y
        return sum, sub     # This can also be written as return (sum, sub) but the parens are redundant
    print(sum_and_sub(1, 2))    # (3, -1)

    """
    We can also assign a function to a var, and then that var will be treated as a func
    """
    def get_my_sum (x, y, z):
        return x+y+z
    new_sum = get_my_sum    # Here, we assign get_my_sum to a new var, we can use that var as a function
    print("my new sum =", new_sum(1, 2, 3))     # my new sum = 6

    """
    A new note about the param list when defining a function in Python
        def my_function (x, y, *var_args_tuple, **keyword_args)
            statements
    Here 
        1, x, y are treated as normal params
        2, *vargs is a tuple of variable length, that is we can pass as many args to the arg-list as we want
        3, **keyword_args is treated as dictionary, that is when passing args, we must specify name and value of args
    
    E.G: We're calling my_function above
        my_function (1, 2, 3, 4, 5, a=6, b=10)
    1, 2 will be automatically referred to x and y 
    3, 4, 5 will be referred to *var_args_tuple
    a=6, b=10 will be referred to **keyword_args
    
    
    The following func will print out this result
        sum of x and y =  3
        sum of vargs =  18
        name Van
        age 19
        
    """

    def my_sum (x, y, *vargs, **kwargs):
        print("sum of x and y = ", x+y)
        sum = 0
        for var in vargs:
            sum = sum + var
        print("sum of vargs = ", sum)
        for key in kwargs:
            print(key, kwargs.get(key))  # function get(x) of dictionary return the value of the key if present in the
            #                         dict which is different from function values()
            # kwargs.values(): to return a new view object that contains a list of all the values associated
            # with the keys in the dictionary   ->> return: dict_values(['Van', 19])

    my_sum(1, 2, 3, 4, 5, 6, name="Van", age=19)    # 3  18 Van 19



















