import math

"""
    These functions are to check if a number is palindrome or not.
    Palindrome means that the reverse of a string/num is the same as that string/num
    E.g: 12321, 1, aba, etc.
"""


def get_reverse_num1(num: int) -> int:
    """
        1. Turn the num to a string
        2. Reverse the string
        3. Cast the string back to a num
    """
    string_num = str(num)
    new_string_num: str = ""
    n = len(string_num)
    for i in range(0, n):
        new_string_num = new_string_num + string_num[n-1-i]
    reverse_num = int(new_string_num)
    return reverse_num


def is_palindrome_num1(num: int) -> bool:
    """
        Check palindrome by the result of num - reverse_num = 0 or not
    """
    reverse_num = get_reverse_num1(num)
    if reverse_num - num == 0:
        return True
    else:
        return False


def get_digit_list(num: int) -> list[int]:
    """
        Get a list of all the digits existing in the input number
    """
    digit_list = []
    while num != 0:
        remainder = num % 10
        digit_list.append(remainder)
        num = math.floor(num / 10)
    return digit_list


def get_reverse_num2(num: int) -> int:
    digit_list = get_digit_list(num)
    n = len(digit_list)
    reverse_num = digit_list[n-1]
    for i in range(0, n-1):
        reverse_num = reverse_num + digit_list[i] * 10 ** (n-1-i)
        x = 0
    return reverse_num


def get_reverse_num3(num: int) -> int:
    """
        get reverse_num by making use of digit_list, to get a reverse number, we reverse the way that we get the
        remainder list. To get remainder list, we divide the number by 10 and get the remainder. Now, to get the number,
        we multiply the remainder by 10 and then plus the next remainder
    """
    digit_list = get_digit_list(num)
    reverse_num = 0
    for i in range(0, len(digit_list)):
        reverse_num = reverse_num * 10 + digit_list[i]
    return reverse_num


def is_palindrome_num2(num: int) -> bool:
    """
        Check palindrome by using the list of digit

        1. Get the digit list by using get_digit_list()
        2. Check if the left digit is the same as the right digit or not
    """
    digit_list = get_digit_list(num)
    n = len(digit_list)
    if n == 0:
        return False

    left = 0
    right = n - 1
    i = 0
    while left + i < right - i:
        if digit_list[left + i] != digit_list[right - i]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    print(get_digit_list(123))

    print(get_reverse_num2(123))
    print(get_reverse_num3(123))

    print(is_palindrome_num2(123))
    print(is_palindrome_num2(3))
    print(is_palindrome_num2(23))
    print(is_palindrome_num2(12321))




