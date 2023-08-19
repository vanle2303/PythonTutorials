def factorial_with_iteration(num: int) -> int:
    val = 1
    i = 1
    while i <= num:
        val = val * i
        i += 1
    return val


def factorial_with_recursion(num: int) -> int:
    if num <= 1:
        return 1
    return num * factorial_with_recursion(num-1)


if __name__ == '__main__':
    print(factorial_with_iteration(3))
    print(factorial_with_iteration(0))
    print(factorial_with_iteration(5))

    print(factorial_with_recursion(3))
    print(factorial_with_recursion(0))
    print(factorial_with_recursion(5))



