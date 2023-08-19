import math


class BinarySearch:
    """
    This class consists of all functions that to check if a char/int is in a given sorted list or not
    Normally we can use for loop to test through all the elements in the list, but this way is very costly
    Therefore, we choose to break the sorted list into half and just compare our target value with the middle value of
    given list
    """
    def binary_search(self, val, lis: list) -> int:
        """
        This function is for users. They can just simply pass the target and the list, the rest of work, let
        __binary_search_recursively deal with it.
        """
        # return self.__binary_search_recursively(val, lis, 0, len(lis)-1)
        return self.__binary_search_iteratively(val, lis)

    def __binary_search_recursively(self, target: int, lis: list[int], left: int, right: int) -> int:
        """
        This function is for programmers, it is set to be private
        This func is to check if a target is in a list or not. If yes, return the target's index in the list. Otherwise,
        return -1
        The basic steps of this function is:
            1. Break the list into half
            2. Compare the target with the middle value of the list
                a, if target> middle: compare target with the second half of the list
                b, otherwise: compare target with the first half of the list
            And working in this process recursively until meeting the stopping condition

        :param target:
        :param lis:
        :param left: first index of the list
        :param right: last index of the list
        :return: an int
        """
        middle = math.ceil((right+left)/2)
        if target == lis[middle]:       # Stopping condition
            return middle
        if (right-left) == 1:           # Stopping condition
            if target == lis[right]:
                return right
            elif target == lis[left]:
                return left
            else:
                return -1
        if target > lis[middle]:        # Recursively
            return self.__binary_search_recursively(target, lis, middle, right)
        else:                           # Recursively
            return self.__binary_search_recursively(target, lis, left, middle)

    def __binary_search_iteratively(self, target: int, lis: list[int]) -> int:
        """
        This func does the same thing as __binary_search_recursively() but in an iterative way
        Here we use while loop: while left < right, continue testing other half of the list
        :param target:
        :param lis:
        :return:
        """
        left = 0
        right = len(lis)-1
        while left < right:
            middle = math.ceil((right + left) / 2)
            if target == lis[middle]:   # Stopping condition
                return middle
            if (right - left) == 1:     # Stopping condition
                if target == lis[right]:
                    return right
                elif target == lis[left]:
                    return left
                else:
                    return -1
            if target < lis[middle]:
                right = middle   # Now we only test the 1st half of list->Change the right index of the list to `middle`
            else:
                left = middle    # Now we only test the 2nd half of list->Change the left index of the list to `middle


if __name__ == '__main__':
    lis = [1, 2, 3, 5, 9]
    binary_search = BinarySearch()
    print(binary_search.binary_search(0, lis))
    print(binary_search.binary_search(15, lis))
    print(binary_search.binary_search(3, lis))
    print(binary_search.binary_search(6, lis))
    print(binary_search.binary_search(1, lis))





