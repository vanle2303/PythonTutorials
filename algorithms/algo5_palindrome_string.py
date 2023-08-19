import math


def is_palindrome_string1(string: str) -> bool:
    """
        Palindrome String is a string that the reserve of it is the same as the string
    """
    length = len(string)

    if length == 0:
        return False

    middle = math.ceil(length/2)
    left = 0
    right = length - 1
    for i in range(0, middle):
        if string[left+i] != string[right-i]:
            return False
    return True


def is_palindrome_string2(string:str) -> bool:
    """
    This way is just to make use of left and right variables as the indices of a string
    """
    n = len(string)
    if n == 0:
        return False

    left = 0
    right = n - 1
    i = 0
    while left+i < right-i:
        if string[left+i] != string[right-i]:
            return False
        i += 1
    return True


def is_palindrome_string3(string: str) -> bool:
    """
    This is the most effective way that we can get rid of middle, left and right variables
    """
    n = len(string)
    if n == 0:
        return False
    i = 0
    while i < n-1-i:
        if string[i] != string[n-1-i]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    string1 = "abcba"
    string2 = "a"
    string3 = "aba"
    string4 = ""
    string5 = "abcab"
    # string6 = None
    print(is_palindrome_string1(string1))
    print(is_palindrome_string1(string2))
    print(is_palindrome_string1(string3))
    print(is_palindrome_string1(string4))
    print(is_palindrome_string1(string5))

    print()
    print(is_palindrome_string2(string1))
    print(is_palindrome_string2(string2))
    print(is_palindrome_string2(string3))
    print(is_palindrome_string2(string4))
    print(is_palindrome_string2(string5))

    print()
    print(is_palindrome_string3(string1))
    print(is_palindrome_string3(string2))
    print(is_palindrome_string3(string3))
    print(is_palindrome_string3(string4))
    print(is_palindrome_string3(string5))







