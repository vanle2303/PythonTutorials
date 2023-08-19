from collections import deque

from algorithms.algo11_binary_tree import TreeNode

from algorithms.algo11_binary_tree import create_binary_tree


def tree_traversal_bfs_level_by_level(root: TreeNode):
    """
        This function takes a binary tree and print out the tree nodes level by level
        The main idea here is to use 2 parallel queues, one is to store the nodes and another one is to store the
        level corresponding to the node
        Nodes with the same level will be printed out in the same line. Otherwise, we print the node in the next new line

        Here we use the next level as a sign to determine which line we print out the node
    """
    node_queue: deque[TreeNode] = deque([root])
    level_queue: deque[int] = deque([1])

    while node_queue:
        node = node_queue.popleft()
        cur_level = level_queue.popleft()

        left_child = node.get_left()
        right_child = node.get_right()
        # child's level will equal the parent's level plus 1
        next_level = cur_level + 1

        if left_child:
            node_queue.append(left_child)
            level_queue.append(next_level)
        if right_child:
            node_queue.append(right_child)
            level_queue.append(next_level)

        # Here we use the next level as a sign to determine which line we print out the node -> move forward
        if level_queue:
            next_level = level_queue[0]
            # same level, same line
            if cur_level == next_level:
                print(node.value, end=",")
            # different level, next line
            elif cur_level != next_level:
                print(node.value)
        # print the last node, since this node will be corresponded with the previous node, no need to worry abt the
        # line of this node
        else:
            print(node.value)


def tree_traversal_bfs_level_by_level2(root: TreeNode):
    """
        This function is the same as the prev one which takes a binary tree and print out the tree nodes level by level
        The main idea here is to use 2 parallel queues, one is to store the nodes and another one is to store the
        level corresponding to the node

        But here, instead of comparing current level with next level, we compare the previous level with the current one
        Therefore, we need a var to store prev_level with initialization of 0

    """
    node_queue: deque[TreeNode] = deque()
    node_queue.append(root)
    level_queue: deque[int] = deque([1])
    # Here we initialize a previous_level var, which determines the previous level corresponding to the current node
    prev_level = 0

    while node_queue:
        node = node_queue.popleft()
        cur_level = level_queue.popleft()

        left_child = node.get_left()
        right_child = node.get_right()
        next_level = cur_level + 1

        if left_child:
            node_queue.append(left_child)
            level_queue.append(next_level)
        if right_child:
            node_queue.append(right_child)
            level_queue.append(next_level)

        if cur_level == prev_level:
            # If the two levels are equal, we print the node out following by a comma
            print(node.value, end=",")
        else:
            # If the two levels are not equal, we move to a new line and print out the node with a comma
            print()
            print(node.value, end=",")
            # now we assign the current level to the previous level
            prev_level = cur_level


def tree_traversal_bfs_level_by_level3(root: TreeNode):
    """
        This function is the same as the 2 prev ones which takes a binary tree and print out the tree nodes level by level
        The main idea here is to use 2 parallel queues, one is to store the current_level nodes and
        another one is to store the next-level nodes (the children of the current node)
    """
    cur_level_nodes: deque[TreeNode] = deque()
    cur_level_nodes.append(root)
    next_level_nodes: deque[TreeNode] = deque()

    while cur_level_nodes:
        node = cur_level_nodes.popleft()

        left_child = node.get_left()
        right_child = node.get_right()

        # The left/right child will be appended into the next_level queue
        if left_child:
            next_level_nodes.append(left_child)
        if right_child:
            next_level_nodes.append(right_child)

        # If there are nodes left in next-level queue, print the node value with ","
        if cur_level_nodes:
            print(node.value, end=",")
        # else, print the node value and move to new line
        else:
            print(node.value)
            # BE CAREFUL these assignments since those queues are object not primitive, so we're working with reference
            # If we assign curr = next, then next.clear(), both curr and next will refer to an empty box
            temp = cur_level_nodes
            cur_level_nodes = next_level_nodes
            next_level_nodes = temp


if __name__ == '__main__':
    root_node = create_binary_tree()

    tree_traversal_bfs_level_by_level(root_node)    # 1
                                                    # 2,3
                                                    # 4,5,6,7
                                                    # 8,9

    tree_traversal_bfs_level_by_level2(root_node)   # 1,
                                                    # 2,3,
                                                    # 4,5,6,7,
                                                    # 8,9,

    print()
    print()

    tree_traversal_bfs_level_by_level3(root_node)   # 1,
                                                    # 2,3,
                                                    # 4,5,6,7,
                                                    # 8,9,


