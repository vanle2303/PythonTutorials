"""
    Given a list of strings, get the longest common prefix of those strings
    E.g: ["flower", "flow", "floor"]  -> "flo"
"""


def get_min_length_str(lis: list[str]) -> str:
    if not lis:
        return ""
    min_string = lis[0]
    for i in range(1, len(lis)):
        if len(min_string) > len(lis[i]):
            min_string = lis[i]
    return min_string


def longest_common_prefix1(lis: list[str]) -> str:
    if not lis:
        return ""

    result_str = ""
    min_string = get_min_length_str(lis)
    for i in range(0, len(min_string)):
        char = min_string[i]
        for j in range(0, len(lis)):
            if lis[j][i] != char:
                return result_str
        result_str = result_str + char
    return result_str


def longest_common_prefix2(lis: list[str]) -> str:
    if not lis:
        return ""

    result_str = ""
    first_string = lis[0]
    char = ""
    for i in range(0, len(first_string)):
        char = char + first_string[i]
        for j in range(0, len(lis)):
            if lis[j].find(char) != 0:
                return result_str
        result_str = result_str + first_string[i]
    return result_str


if __name__ == '__main__':
    lis = ["flower", "flow", "floor"]
    print(get_min_length_str(lis))
    print(longest_common_prefix2(lis))
    print(longest_common_prefix1(lis))

    lis2 = ["dog", "racecar", "car"]
    print(longest_common_prefix1(lis2))
    print(longest_common_prefix2(lis2))