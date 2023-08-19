from collections import deque

from algorithms.algo11_binary_tree import TreeNode

from algorithms.algo11_binary_tree import create_binary_tree


def tree_traversal_bfs_with_coordinate(root: TreeNode):
    """
        This function is to print out the node value corresponding with its depth in the binary tree.
        The 1st root's depth is set to 0
        The result is shown here:
            1 : 0
            2 : -1
            3 : 1
            4 : -2
            5 : 0
            6 : 0
            7 : 2
            8 : -1
            9 : 1

    """
    node_queue: deque[TreeNode] = deque([root])
    breadth_queue: deque[int] = deque([0])

    while node_queue:
        node = node_queue.popleft()
        root_coordinate = breadth_queue.popleft()
        print(node.value, ":", root_coordinate)

        left_child = node.get_left()
        right_child = node.get_right()

        if left_child:
            node_queue.append(left_child)
            left_coordinate = root_coordinate - 1
            breadth_queue.append(left_coordinate)
        if right_child:
            node_queue.append(right_child)
            right_coordinate = root_coordinate + 1
            breadth_queue.append(right_coordinate)


if __name__ == '__main__':
    root = create_binary_tree()
    tree_traversal_bfs_with_coordinate(root)

