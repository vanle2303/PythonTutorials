if __name__ == '__main__':
    a = True
    print(a, type(a))   # True <class 'bool'>

    a = 2
    b = 3
    # The two statement are the same
    print(bool(a == b))
    print(a == b)

    # The following statements will return false when a var equals None, an empty sequence or 0
    a = None
    print(bool(a))

    a = ()
    print(bool(a))

    a = 0
    print(bool(a))

    # But this will return true
    a = 10
    print(bool(a))


