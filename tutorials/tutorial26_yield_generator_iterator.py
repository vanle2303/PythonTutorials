"""
https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/

    1. Any function that have yield is a generator
    2. An iterator is anything that has __iter__() method, which returns an object that has __next__() function

Quick Note:
    1. Iterator: { has function __iter__()
                 { return a generator

    2. Generator function: { return a generator
                           {

    3. Generator: { has function __next__()
                  {

    4. Iterator can also be a generator if it has function __next__()
"""
import time

if __name__ == '__main__':
    def simple_generator_func():
        """
        1. The yield statement suspends a function's execution RIGHT AFTER yield statement and sends the value back to
        the caller, but it also retains enough state to enable the function to resume where it left off
        2. When it resumes, it continues execution immediately AFTER the end of the last yield statement
        [1. and 2. allows its code to produce a series of values OVER time (series of calls), rather than computing it
        once and return the result]
        :return:
        """
        yield 1
        # print("after step 1, before step 2 ") # This step is just to check where yield statement stop
        yield 2
        # print("after step 2, before step 3")
        yield 3     # if try to call the func for more than 3 times, errors occur

    for num in simple_generator_func():
        print(num)  # 1 2 3
        # time.sleep(3)   # This causes the prog to pause/ sleep for some seconds and then resumes

    print(simple_generator_func())  # We cannot just call generator func alone
    #                                <generator object simple_generator_func at 0x10abb34a0>

    # We don't have to use for loop, we can jjust manually call __next__
    gen = simple_generator_func()   # Since this returns a generator, we can use __next__() function to get the yields
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    # print(gen.__next__()) # causes error bc there are only 3 yields

    def next_square():
        """
        This is an infinite generator using while loop
        :return:
        """
        i = 1
        while True:
            yield i*i
            i += 1

    gen1 = next_square()
    # use next() function instead of a loop. next() actually calls __next__() of the generator(polymorphism via func)
    print(gen1.__next__())  # 1
    print(gen1.__next__())  # 4
    print(next_square().__next__())  # 1


    class SimpleIterator:
        """
            https://www.geeksforgeeks.org/iterators-in-python/

        An iterator is anything that has function __iter__() - a generator function.
        Recall that a generator func returns an object that has __next__() function.

        The main idea of Iterator is that a generator can be encapsulated in an obj, instead of calling a generator func
        So basically, inside the __iter__() function, we can just call another generator function and returns its
        returned value
        """

        def __init__(self):
            pass

        def __iter__(self):
            """
            Here we need to return a generator or basically return sth that has __next__() function
            Therefore, we just call simple_generator_func() since it is a generator function
            """
            return simple_generator_func()

    # now we can just use the for loop for an iterator
    simple_iterator = SimpleIterator()  # simple_iterator is now treated as a generator
    for i in simple_iterator:
        print(i, end=", ")  # 1, 2, 3,

    class SquareIterator:
        """
        Here is a class itself has __iter__() function. Therefore, it is treated as a iterator.
        It also has __next__() function, therefore, it is a generator itself
        """

        def __init__(self, limit: int):
            self.limit = limit

        def __iter__(self):     # so this is an iterator since it has __iter__() function
            self.i = 1
            # Since it is a gen func, we have to return a generator here
            # However, this class is also a generator bc it has __next__(). Therefore, we can return self
            return self

        def __next__(self):     # it is also a generator since it has __next__() function
            """
            NOTE: We don't need to use yield here.Yield is used to return a generator (sth that has __next__ function)
            Here we are inside the __next__ function already. Therefore, in iterator class, we don't need to use yield
            """
            value = self.i * self.i
            if value > self.limit:
                raise StopIteration

            self.i += 1
            return value

    print()
    square_iterator = SquareIterator(25)    # set the limit value to 25,so if returned result exceeds 25,stop iterating
    for i in square_iterator:
        print(i, end=", ")      # 1, 4, 9, 16, 25,







