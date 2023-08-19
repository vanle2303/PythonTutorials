"""
In Python, polymorphism can be achieved through classes like in Java
In addition, it can also be achieved through functions
E.g:
    len() function can take any objects: list, tuple, string, etc.
    The truth is, the len() func calls the len() function of its input object:

        def len(obj):
            return obj.len()

    So it delegates (uy thac) the calls to the function of the input obj, and that's how it can work on so many objs

    Similar to method sorted(), which delegates calls to its input's function sort()

"""

if __name__ == '__main__':
    list = [1, 2, 3]
    dict = {1: 1, 2: 2}
    s = "Hello"

    len(list)
    len(dict)
    len(s)
    # We all know that list, dict, and string all have their own len() function

    # Similarly, the built-in sorted method
    sorted(list)
    list.sort()

    