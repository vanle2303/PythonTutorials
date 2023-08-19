def my_sum(x, y):
    # Python also use local vars and global vars. This is an example of local var
    _sum = x + y
    return _sum


if __name__ == '__main__':
    # Create and print variables
    counter = 100
    miles = 1000
    name = "Van"
    print(counter, miles, name)

    # Delete variables and if we try to use var counter after this step, an error will be thrown
    del counter

    # Multiple assignment
    a = b = c = 100
    print(a)
    print(b)
    print(c)
    a, b, c = 1, 2, 3
    print(a, b, c)

    print(my_sum(1, 2))





