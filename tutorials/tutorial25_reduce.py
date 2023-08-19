import functools
import operator


if __name__ == '__main__':
    """
    https://www.geeksforgeeks.org/reduce-in-python/
    
    Function reduce(func, sequ) is used to apply a particular function passed as its args to all of the list elements
    mentioned in the sequence passed along. This function is defined within module "functools"
    
    Basically, reduce() take 2 params: 1 func and 1 collection.
    reduce() is to at least 1 element each time and return a new element to the collection. This process will continuw
    until there's only one element left in the collection, and that's the return result
    
    Working process:
        1. The first 2 elements of the sequence are picked and the result is obtained
        2. Apply the same function to the previously obtained result and the number just succeeding th second element 
        and the result is again stored
    This process will continue until no more elements are left in the container
    The final result is returned and printer on the console
    """

    list = [1, 2, 3, 4, 5]
    sum = functools.reduce(lambda x, y: x + y, list)
    print(sum)  # 15

    def prod(x, y):
        return x*y

    product = functools.reduce(prod, list)
    print(product)

    # We can also use operators which have a bunch of functions already
    my_product = functools.reduce(operator.mul, list)
    print(my_product)

    my_sum = functools.reduce(operator.add, list)
    print(my_sum)