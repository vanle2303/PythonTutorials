from collections import deque

from algorithms.algo11_binary_tree import TreeNode

from algorithms.algo11_binary_tree import create_binary_tree


def tree_traversal_bfs_queue(root_node: TreeNode):
    """
        bfs stands for Breadth first search, which means we traverse the tree from the first level to the next one,
        like traverse tung tang mot a

        Queue: First In First Out ->>> Append right and pop left. So we use append() and popleft() for queue
        We use deque to create a queue that can pop from both 2 ends
    """
    node_queue: deque[TreeNode] = deque()
    node_queue.append(root_node)
    while node_queue:
        node = node_queue.popleft()
        print(node.value, end=",")

        left_child = node.get_left()
        right_child = node.get_right()

        if left_child:
            node_queue.append(left_child)
        if right_child:
            node_queue.append(right_child)


if __name__ == '__main__':
    root_node = create_binary_tree()
    tree_traversal_bfs_queue(root_node)  # 1,2,3,4,5,6,7,8,9,
