"""
Python supports several types of operators:
    1, Arithmetic operators: (+)  (-)  (*)  (/)  (%):modules  (**):exponent-> 4**2=16, (//):floor division-> 9//2=4
    2, Comparison operators: (==)  (!=)  (>)  (<)  (>=)  (<=)
    3, Assignment operators: (=)  (+=)  (-=)  (*=)  (/=)  (%=)  (**=)  (//=)  =>> This is the same as in Java
    4, Bitwise operators: Bitwise operators work on bits and performs bit by bit operation
            a, & (Binary AND): Sets each bit to 1 if both bits are 1
            b, | (Binary OR): Sets each bit to 1 if one of two bits is 1
            c, ^ (Binary XOR): Sets each bit to 1 if only one of two bits is 1
            d, ~ (Binary Ones Complement): Inverts all the bits
            e, << (Binary Left Shift): Shift left by pushing zeros in from the right and let the leftmost bits fall off
            f, >> (Binary Right Shift): Shift right by pushing copies of the leftmost bit in from the left,
                                        and let the rightmost bits fall off
    5, Logical operators: AND/ OR/ NOT
    6, Membership operators: in/ not in
    7, Identification operators: is/ is not

"""

if __name__ == '__main__':
    # Arithmetic operators
    a = 11
    b = 2
    print("a + b = ", a + b)    # 13
    print("a % b = ", a % b)    # 1  ->> Modules
    print("a ** b = ", a ** b)  # 121 ->> Exponent: a to the power of b
    print("a // b = ", a // b)  # 5  ->> Floor division

    # Comparison operators
    a = 1
    b = 2
    print(a == b)   # False
    print(a > b)    # False
    print(a < b)    # True

    # Assignment operators
    a = 10
    a += 5
    print("a += 5: ", a)    # a += 5:  15
    a *= 2
    print("a *= 2: ", a)    # a *= 2:  30

    # Bitwise operators
    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    # & (Binary AND): Sets each bit to 1 if both bits are 1
    c = a & b   # 12 = 0000 1100 ->> Set bits first, Then get 61 from the bits sign
    print(c)    # 12
    # ^ (Binary XOR): Sets each bit to 1 if only one of two bits is 1
    c = a ^ b   # # 49 = 0011 0001
    print(c)
    # << (Binary Left Shift)
    c = a << 2
    print(c)    # # 240 = 1111 0000

    # Logical operators: AND/ OR/ NOT
    a = True
    b = False
    c = True
    print(a and b)  # False
    print(a or b)   # True
    print(a or c)   # True
    print(not a)    # False

    # Membership operators: in/ not in
    list1 = [1, 2, 3]
    print(1 in list1)   # True
    print(4 in list1)   # False

    # Identification operators: is/ is not
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1]
    print(list1 == list2)   # True
    print(list1 is list2)   # False
    print(id(list1))    # 4301295808  ->> Function id() returns the id of an obj
    print(list1 is not list2)   # True
    print(list3 in list1)   # False















