"""
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    Note: a word is said to be a string of chars with white space at the 2 ends
        A string may have white spaces in the end, those spaces are not counted as our last word

"""


def get_last_word(string: str) -> str:
    n = len(string)
    last_word_reverse = ""
    last_word = ""
    for i in range(n-1, -1, -1):
        if string[i] != " ":
            last_word_reverse = last_word_reverse + string[i]
        elif last_word_reverse:
            break

    for j in range(len(last_word_reverse)-1, -1, -1):
        last_word = last_word + last_word_reverse[j]

    return last_word


def length_of_last_word1(string: str) -> int:
    last_word = get_last_word(string)
    length = len(last_word)
    return length


def length_of_last_word2(string: str) -> int:
    n = len(string) - 1
    count = 0
    while n >= 0:
        if string[n] != " ":
            count += 1
        elif string[n] == " " and count != 0:
            return count
        n -= 1
    return count


def length_of_last_word3(string: str) -> int:
    n = len(string) - 1
    count = 0
    letter_seen: bool = False
    while n >= 0:
        if string[n] != " ":
            count += 1
            letter_seen = True
        else:
            if letter_seen:
                return count
            else:
                pass
        n -= 1
    return count


if __name__ == '__main__':
    string1 = "Hello World"
    string2 = "Hello World "
    string3 = "Hello World   "

    print(get_last_word(string1))
    print(length_of_last_word1(string1))
    print(length_of_last_word2(string1))
    print(length_of_last_word3(string1))

    print()
    print(length_of_last_word1(string2))
    print(length_of_last_word2(string2))
    print(length_of_last_word3(string2))

    print()
    print(length_of_last_word1(string3))
    print(length_of_last_word2(string3))
    print(length_of_last_word3(string3))

