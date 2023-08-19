"""
    https://leetcode.com/problems/two-sum/description/
Given an array of integers nums and an integer called target, return indices of the two numbers such that they add up to target
You may assume that each input would have exactly one solution, and you may not use the same element twice.

E.g: Input: nums = [2,7,11,15], target = 9
     Output: [0,1]
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Here we use two nested loops: i (0 --> n-1) and j (i+1 --> n).
    If the sum equals the target, return. Else continue the loop
    Since for each value of i returns n times to loop through j. The complexity of this method is O(n^2)
    """
    result_list = []
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result_list.append(i)
                result_list.append(j)
                return result_list
    # If it reaches this point, then NO 2 nums found, we still must return an empty list
    # If we skip the return statement, then the func would return None
    return result_list


def get_index_map(nums: list[int]) -> dict[int, set[int]]:
    """
    This function takes a list of nums and return a dictionary with the key is the elements of input list and
    the value is a set of that element's indices in the list
    This is similar to the frequency map we did in Java, but this one has more details, we can easily get the frequency
    from this
    :param nums:
    :return:
    """
    index_map = {}
    for i in range(len(nums)):
        val = nums[i]
        if val not in index_map:
            index_set = set()
            index_set.add(i)
            index_map[val] = index_set
        else:
            index_set = index_map[val]
            index_set.add(i)
    return index_map


def two_sum_efficient(nums: list[int], target: int) -> list[int]:
    """
    This is a much more effective way to solve this prob, whose complexity is just O(n)
    This approach consists of 2 steps:
        1. get_index_map(): a dictionary with the key is the elements of input list and the value is a set of that element's
           indices in the list
        2. two_sum_efficient(): main idea is for each number x in the list:
            - fin the complement target - x
            - check in the index_map if this complement is a key (O(1))
               - if exists, simply get an index from the index_set, that is different from the index of x
               - otherwise, move to the next x

    NOTE: We use break 2 times in this code, and the second break is used only if the first break is executed
    So there must be a sign for the second break to be executed. Therefore, we use a common boolean signal as a sign for
    both break statements, that is if the boolean var is True then the second break is executed
    """
    result_list = []
    index_map: dict[int, set[int]] = get_index_map(nums)
    found: bool = False
    for i in range(len(nums)):
        rest = target - nums[i]
        if rest in index_map:
            index_set = index_map[rest]
            for sec_index in index_set:
                if sec_index != i:
                    result_list.append(i)
                    result_list.append(sec_index)
                    found = True    # found is a boolean var that is treated as a sign for the second break to be used
                    break
        if found:
            break   # only use this break when the previous break is executed
    return result_list


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    nums2 = [3, 2, 4]
    nums3 = [3, 3]

    # Test get_index_map()
    test_index_set1 = get_index_map(nums1)
    print("index set:", test_index_set1)
    test_index_set2 = get_index_map(nums2)
    print("index set:", test_index_set2)
    test_index_set3 = get_index_map(nums3)
    print("index set:", test_index_set3)
    print()

    test1a = two_sum(nums1, target=9)
    test1b = two_sum_efficient(nums1, target=9)
    print(test1a)
    print(test1b)
    print()

    test2a = two_sum(nums2, target=6)
    test2b = two_sum_efficient(nums2, target=6)
    print(test2a)
    print(test2b)
    print()

    test3a = two_sum(nums3, target=6)
    test3b = two_sum_efficient(nums3, target=6)
    print(test3a)
    print(test3b)


