"""
range works like a for loop in Java
general form: range(start, stop, step)
    1. start: int number to specify the starting point (optional)
    2. stop: int number to specify the stopping point, result wil exclude the stop val (mandatory)
    3. step: int number to specify the increment (optional, default: 1)
"""

if __name__ == '__main__':
    for i in range(5):
        print(i)    # 0, 1, 2, 3, 4

    for i in range(1, 5):
        print(i)    # 1, 2, 3, 4

    for i in range(1, 5, 2):
        print(i)    # 1, 3

    for c in "Hello":
        print(c)    # H, e, l, l, o
