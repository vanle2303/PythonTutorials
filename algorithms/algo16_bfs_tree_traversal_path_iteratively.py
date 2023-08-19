from collections import deque

from algorithms.algo11_binary_tree import TreeNode

from algorithms.algo11_binary_tree import create_binary_tree


def get_paths_of_a_binary_tree_iteratively(root: TreeNode):
    node_and_path_queue: deque[tuple[TreeNode, list[TreeNode]]] = deque([(root, [root])])
    result_path: list[list[int]] = []

    while node_and_path_queue:
        node_path_tuple = node_and_path_queue.popleft()
        node = node_path_tuple[0]
        path = node_path_tuple[1]

        left_child = node.get_left()
        right_child = node.get_right()

        if not left_child and not right_child:
            value_path: list = []
            for nodes in path:
                value_path.append(nodes.value)
            result_path.append(value_path)

            # for node in path:
            # print(node.value, end=",")

        if left_child:
            left_path = path.copy()
            left_path.append(left_child)
            node_and_path_queue.append((left_child, left_path))
        if right_child:
            right_path = path.copy()
            right_path.append(right_child)
            node_and_path_queue.append((right_child, right_path))

    return result_path


if __name__ == '__main__':
    root = create_binary_tree()
    print(get_paths_of_a_binary_tree_iteratively(root))     # [[1, 2, 4], [1, 3, 7], [1, 2, 5, 8], [1, 3, 6, 9]]

