from collections import deque


class ListNode:
    def __init__(self, value: int, next = None):
        self.value = value
        self.__next = next

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next


def create_linked_list():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.set_next(node2)
    node2.set_next(node3)
    node3.set_next(node4)
    node4.set_next(node5)
    node5.set_next(node6)

    return node1


def print_node_list_iteratively(head: ListNode):
    curr_node = head
    while curr_node:
        print(curr_node.value, end=",")
        curr_node = curr_node.get_next()


def print_node_list_recursively(head: ListNode):
    print(head.value, end=",")
    next = head.get_next()
    if next:
        print_node_list_iteratively(next)


if __name__ == '__main__':
    root = create_linked_list()

    print("Iterative: ")
    print_node_list_iteratively(root)   # 1,2,3,4,5,6,
    print()

    print("Recursive: ")
    print_node_list_recursively(root)   # 1,2,3,4,5,6,




