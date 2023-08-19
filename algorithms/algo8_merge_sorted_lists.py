def merge_sorted_lists(lis1: list[int], lis2: list[int]) -> list[int]:
    """
        You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list

    """

    # This is to test either lis1 or lis2 is empty, we return the other list
    if not lis1:
        return lis2
    if not lis2:
        return lis1

    result_lis = []
    i = 0
    j = 0

    # Here, we use a while loop to compare the elements from lis1 with lis2
    # The main idea is:
    #   1. Compare lis1[0] vs lis2[0]
    #   2. If lis1[0] < lis2[0], push lis1[0] into the result list
    #   3. Then compare lis1[1] vs lis2[0]
    # The smaller value will be pushed into the result list and we move to compare the next value of the list

    while i < len(lis1) and j < len(lis2):
        if lis1[i] <= lis2[j]:
            result_lis.append(lis1[i])
            i += 1
        else:
            result_lis.append(lis2[j])
            j += 1

    # At this step, either lis1 or lis2 is done with looping through all its elements and all of its elements are pushed
    # into the result list
    # Now we just need to check which list still has elements that are not tested
    # Therefore, we need to test the value of i and j

    if j < len(lis2):   # means lis2 still has some non-tested elements
        for k in range(j, len(lis2)):
            result_lis.append(lis2[k])
    elif i < len(lis1):  # means lis1 still has some elements left
        for k in range(i, len(lis1)):
            result_lis.append(lis1[k])

    return result_lis


if __name__ == '__main__':
    lis1 = [1, 100]
    lis2 = [2, 2, 4]
    print(merge_sorted_lists(lis1, lis2))

    lis3 = [1, 3, 5, 10]
    lis4 = [2, 3, 6]
    print(merge_sorted_lists(lis3, lis4))

    lis5 = [1]
    lis6 = []
    print(merge_sorted_lists(lis5, lis6))
