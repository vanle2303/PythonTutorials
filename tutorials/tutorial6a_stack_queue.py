#!/usr/bin/python3
"""
In Python, in order to run a program, we have to provide it an interpreter/executor. Normally, we use python3 as an
interpreter
But twe don't want to rewrite python3 every time we run our prog. Therefore, statement #!/usr/bin/python3 takes in place
That is, when running a prog in Terminal and we declare "python3 file-name", Python will execute prog by using python3.
Now  #!/usr/bin/python3 is treated as a comment.
However, if we don't declare python3 and just provide file-name, Python will go all the way back to the beginning of the
file and if it see #!/usr/bin/python3, it will execute using python3 as an interpreter

When writing a file, it often has some specific permissions like write, read, execute (w,r,x). Normally, a file has
read-only permission for everyone. In order to change the permission mode, we use
    1. "chmod +x" (update executable mode)
    2. "which file-name" to see the permission mode of a file,
    3. " ./file-name" to run a file
"""

from collections import deque

if __name__ == '__main__':
    """
    Use list for stack bc the pop() function is very efficient in popping the last element
    However, list.pop() is no more efficient in popping the first element bc it needs to shift the entire array to the
    left.
    Therefore, for queue, we use deque instead. deque is fast and efficient in adding and popping from both ends 
    """

    # Here we're abt to use deque as stack. Stack: First In Last Out ->>> Append right and pop right
    # So we just simply use append() and pop() for stack
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print(stack)    # [1, 2, 3, 4]
    stack.pop()     # now pop the last added element: 4
    print(stack)    # [1, 2, 3]

    # Here we're working with deque as queue. Queue: First In First Out ->>> Append right and pop left
    # So we use append() and popleft() for queue
    queue: deque[int] = deque()     # deque() is a constructor to create a deque obj: A list-like sequence optimized
    queue.append(1)                 # for data accesses near its endpoints.
    queue.append(2)
    # queue.appendleft(0)     # Though we have appendleft(), we don't really use it in reality
    queue.append(3)

    print(queue)            # deque([0, 1, 2, 3])
    # print(queue.popleft())  # 0 ->> the last added to the left
    print(queue.pop())


