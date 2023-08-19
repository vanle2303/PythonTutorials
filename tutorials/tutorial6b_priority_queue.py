import heapq

if __name__ == '__main__':
    """
    What is "priority heap"? - The element with the highest value will have the highest priority and likewise the one 
    with the lowest value will have the lowest priority
    
    Use heap module for priority queue in Python. It is a min heap
    It operates on a given list, so every functions need to take a list as one of the args
    It has only 5 functions:
        1. heapify() : call this function first to create a heap on a given heap
        2. We then call: heappop(), heappush(), etc.
        
    Note: This is working with min heap.
    To get a max heap, simply invert number to negative, such as 100 -> -100, before pushing into the heap
    
    So why we use min/max heap instead of a normal array? - Complexity
    That is bc to push elements into a heap costs O(n) and to pop elements out of a heap just costs O(1), which is very 
    cheap. But with array, it costs O(n*log(n)) to push, which is very costly
    
    Min/max heap sorts the list in its own way but it always ensures that the highest/lowest value is placed 
    at the beginning of the list, and the rest will be sorted in some unknown order.
    After the lowest/highest value is popped out of the list, the heap continues its work to ensure that the next
    high/low value will replace the popped value to become the new highest/lowest value of the list. 
    And the order of remaining elements is still unknown
    """

    list = [3, 4, 1, 5, 8, 2]
    heapq.heapify(list)
    print(list)     # [1, 4, 2, 5, 8, 3]

    print(heapq.heappop(list))  # 1
    print(list)     # [2, 4, 3, 5, 8]

    heapq.heappush(list, 0)
    print(list)     # [0, 4, 2, 5, 8, 3]

    heapq.heappushpop(list, 1)  # push the item onto the list then pop and return the lowest element of the list
    print(list)     # [1, 4, 2, 5, 8, 3]

    three_smallest = heapq.nsmallest(3, list)   # get the three smallest values of the list
    print(three_smallest)   # [1, 2, 3]
    three_largest = heapq.nlargest(3, list)     # get the three largest values of the list
    print(three_largest)    # [8, 5, 4]

    print(list)     # [1, 4, 2, 5, 8, 3]  ->> heap remains the same
    smallest = heapq.heapreplace(list, 10)  # pop and return the currently smallest value and then add the new item
    print(smallest)     # 1
