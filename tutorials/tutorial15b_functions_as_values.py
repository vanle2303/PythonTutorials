"""
In Python, we can also use a function as a variable and pass a function to another function
"""


def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def compute(x, y, func):  # This uses a function as a param to another function
    return func(x, y)


sum = compute(1, 2, sum)  # This is NOT CALLING a function but to pass a function as an arg to other func
print(sum)  # 3               Now func sum is treated as a normal var

sub = compute(1, 2, sub)
print(sub)  # -1

"""
In Python, we can also define a func in another function and return a function
"""


def compute_sum(x):
    def add(y):  # This is to define a function in another function
        return x + y

    return add  # This is to return a function as a result of a function


# Here is how we call function compute_sum
my_func = compute_sum(3)  # Now my_func is really a function since compute_sum returns a func
sum = my_func(2)  # my_func is treated as func add() defined inside compute_sum
print(sum)  # 5