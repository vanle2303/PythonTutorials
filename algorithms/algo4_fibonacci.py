def fibo_with_iterative(num: int) -> list[int]:
    """
    This function is to print out the first nth elements of the fibonacci sequence using iteration
    """
    fibo_list: list[int] = []
    i = 1
    while i <= num:
        val = fibo(i)
        fibo_list.append(val)
        i += 1
    return fibo_list


def fibo(num: int):
    if num <= 0:
        raise Exception("Input must be positive")
    if num == 1 or num == 2:
        return 1
    return fibo(num-1) + fibo(num-2)


def fibo_with_iterative_efficient(num: int) -> list[int]:
    if num <= 0:
        raise Exception("Input must be positive")
    if num == 1:
        return [1]

    fibo_list = [1, 1]
    if num == 2:
        return fibo_list

    i = 2
    while i < num:
        val = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(val)
        i += 1
    return fibo_list


if __name__ == '__main__':
    print(fibo(5))
    print(fibo_with_iterative(0))
    print(fibo_with_iterative(4))
    print(fibo_with_iterative(5))
    print(fibo_with_iterative(8))
    print("Hello")

    # print(fibo_with_iterative_efficient(0))
    print(fibo_with_iterative_efficient(1))
    print(fibo_with_iterative_efficient(2))
    print(fibo_with_iterative_efficient(3))
    print(fibo_with_iterative_efficient(5))
    print(fibo_with_iterative_efficient(8))





