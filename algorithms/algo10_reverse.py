import math


class Reverse:
    def __init__(self):
        pass

    def simple_reverse1(self, string: str) -> str:
        """
            This function simple reverses a string, like from "abcde" to "edcba"
            Time complexity: O(n)
            Memory complexity: O(n) since we have to create a new string to save all the element of the input string
        """
        reverse_string = ""
        n = len(string)
        for i in range(n-1, -1, -1):
            reverse_string = reverse_string + string[i]
        return reverse_string

    def simple_reverse_list1(self, lis: list[str]) -> str:
        left = 0
        right = len(lis) - 1
        middle = math.floor((left+right)/2)
        for i in range(0, middle+1):
            char = lis[i]
            lis[i] = lis[right-i]
            lis[right-i] = char
        return lis

    def simple_reverse_list_using_left_right_indices(self, lis: list[str]) -> list[str]:
        left = 0
        right = len(lis) - 1
        while left < right:
            temp = lis[left]
            lis[left] = lis[right]
            lis[right] = temp
            left += 1
            right -= 1
        return lis

    def get_words(self, list_of_chars: list[str]) -> list[list[str]]:
        """
            This function takes a list of string and then return a list of lists of strings
            Basically, each string is a character since in Python a character is a string
            A list of string is referred to as a word
            A list of lists of strings is a full sentence
        """
        list_of_words: list[list[str]] = []    # a list of characters (In Python, a char is a string)
        n = len(list_of_chars)
        create_new_word: bool = True
        for i in range(0, n):
            char = list_of_chars[i]

            # Here we need to adjust our condition so that we won't create a new empty word every time me meet " "and ""
            # consecutively. It's just a waste of memory
            # But in this example, these statements don't matter that much
            if create_new_word:
                word = []
                create_new_word = False

            if char == " " or char == "":
                if word:
                    create_new_word = True
            else:
                word.append(char)

            if word and (create_new_word or i == n-1):
                # if we already have a word and (need to create a new one or we come to the end of the list)
                # we have to append that word into the result list
                list_of_words.append(word)

        return list_of_words

    def reverse_sentence(self, list_of_char: list[str]) -> list[list[str]]:
        list_of_word = self.get_words(list_of_char)
        left = 0
        right = len(list_of_word) - 1
        while left < right:
            word = list_of_word[left]
            list_of_word[left] = list_of_word[right]
            list_of_word[right] = word
            left += 1
            right -= 1
        return list_of_word


class ReverseEveryKChar:
    """
        This class demos functions that are to reverse every k element of an input string
        There are several ways to approach this prob
    """
    def __init__(self):
        pass

    def reverse_sub_string(self, string_list: list[str], left: int, right: int):
        """
            This func takes a string and reverse a sub string of the input string
            The sub string is from index left to right of the input string
        """
        while left < right:
            char = string_list[left]
            string_list[left] = string_list[right]
            string_list[right] = char
            left += 1
            right -= 1

    def reverse_string_huy_logic(self, string: str, k: int):
        # This step is to convert a string into a list of strings
        string_list: list[str] = []
        for i in range(0, len(string)):
            string_list.append(string[i])

        left = 0
        right = left + k - 1
        while right < len(string_list):
            # Here we call reverse_sub_string() written above to reverse sub-string from given indices
            # This function is actually a while loop
            self.reverse_sub_string(string_list, left, right)

            # after the call of reverse_sub_string() is done, we increment values of left and right by k
            left = left + k
            right = right + k

        # func join() is to convert a list into a string and it returns a string
        # This is a very efficient way that we dont have to create a new array any time we add a new char/elem into the
        # existed string
        # e.g: string = "a"   string = string + "b"  -> these statements will create a new string to store "ab"
        # not just append b into "a"
        reverse_string = "".join(string_list)
        return reverse_string

    def reverse_every_k_element_van_logic(self, string: list[str], k: int):
        """
            This is another way to reverse every k element of a string
            This is pretty much a combination of the 2 previous functions
            This is an inplace function, which means that we make changes right inside the string instead of creating
            a new empty string and add elements into the new one
        """
        left = 0
        right = left + k - 1
        while right < len(string):
            # Here we have to save the values of left and right, since later on we need to use their original values
            prev_left = left
            prev_right = right
            while left < right:
                char = string[left]
                string[left] = string[right]
                string[right] = char
                left += 1
                right -= 1
            left = prev_left + k
            right = prev_right + k

    def reverse_substr(self, list_of_chars: list[str]):
        """
            This function is to reverse a list of strings, this is also alike some of the functions above
        """
        left = 0
        right = len(list_of_chars) - 1
        while left < right:
            char = list_of_chars[left]
            list_of_chars[left] = list_of_chars[right]
            list_of_chars[right] = char
            left += 1
            right -= 1

    def get_list_of_subs(self, string: str, k: int) -> list[list[str]]:
        """
            Here, we would love to take a list of every k element of a string
            So we expect to get list[list[str]]
        """
        # This step is to convert a string into a list of string
        list_of_chars: list[str] = []
        for i in range(0, len(string)):
            list_of_chars.append(string[i])

        # Here, for every k element of the list[string], we group them into a list and push into a supper list hehe
        list_of_subs: list[list[str]] = []
        left = 0
        right = left + k
        while right <= len(list_of_chars):
            sub = list_of_chars[left:right]
            list_of_subs.append(sub)
            left = left + k
            right = right + k

        # If the total number of char can't be divided by k, then we have to deal with the remainder
        # Here is how we do it
        if left < len(list_of_chars):
            sub = list_of_chars[left: len(list_of_chars)]
            list_of_subs.append(sub)

        return list_of_subs

    def reverse_string_van_logic(self, string: str, k: int) -> str:
        """
            This function makes use of the 2 functions above
        """
        # First, we get a list of sub_string, which is list[list[str]]
        list_of_subs = self.get_list_of_subs(string, k)  # e.g: [["1", "2"], ["3", "4"]]

        # Now we're about to reverse all the sub string of the supper list
        for i in range(0, len(list_of_subs)):
            sub_list = list_of_subs[i]
            # Here we call reverse_substr()
            self.reverse_substr(sub_list)   # e.g: [["2", "1"], ["4", "3"]]

        reverse_subs: list[str] = []
        # Here we join element of the substrings together
        for j in range(0, len(list_of_subs)):
            sub = "".join(list_of_subs[j])
            reverse_subs.append(sub)
            # To this step, we have a list of strings like ["21", "43"]

        reverse_string = "".join(reverse_subs)  # "2143"
        return reverse_string


if __name__ == '__main__':
    reverse = Reverse()
    # print(reverse.simple_reverse1("abcde"))

    # print(reverse.simple_reverse_list1(["1", "2", "3", "4", "5"]))
    # print(reverse.simple_reverse_list1(["1", "2", "3", "4"]))

    # print(reverse.reverse_every_k_element("123456", 2))

    # print(reverse.simple_reverse_list_using_left_right_indices(["1", "2", "3", "4", "5"]))
    # print(reverse.simple_reverse_list_using_left_right_indices(["1", "2", "3", "4"]))

    print(reverse.get_words([" ", "", " ", "H", "i", " ", "", "I", " ", "a", "m", " ", "V", "a", "n", " ", "", " "]))
    print(reverse.get_words(["T", "h", "i", "s", " ", "i", "s", " ", "m", "y", " ", "m", "o", "m"]))

    print(reverse.reverse_sentence(["H", "i", " ", "I", " ", "a", "m", " ", "V", "a", "n"]))
    print(reverse.reverse_sentence(["T", "h", "i", "s", " ", "i", "s", " ", "m", "y", " ", "m", "o", "m"]))
    print()

    string = "Hello  I am Van  "
    words = string.split()
    print(words)
    print()

    reverse2 = ReverseEveryKChar()
    string1 = "12345678"
    print("cau logic", reverse2.reverse_string_huy_logic(string1, 4))

    string_list2 = ["1", "2", "3", "4", "5", "6", "7", "8"]
    reverse2.reverse_every_k_element_van_logic(string_list2, 5)
    print(string_list2)
    print()

    test_str = "12345678"
    print(reverse2.get_list_of_subs(test_str, 3))

    print(reverse2.reverse_string_van_logic(test_str, 3))


