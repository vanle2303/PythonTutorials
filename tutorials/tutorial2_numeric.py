"""
Python supports 4 numerical types:
    1. int  (1,10, 100, ...)
    2. long (51924361L, -0x19323L, ...)
    3. float (0.0, 15.3, 100.200, ...)
    4. complex (3.14j, 9.322e-36j)
"""

if __name__ == '__main__':
    a = 100
    print("value of a:", a, "  type:", type(a))

    b = 12.345
    print("value of b:", b, "  type:", type(b))

    c = 10+3j
    print("value of c:", c, "  type:", type(c))