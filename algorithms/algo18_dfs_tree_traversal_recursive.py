from algorithms.algo11_binary_tree import TreeNode

from algorithms.algo11_binary_tree import create_binary_tree


def recursive_tree_traversal_dfs_in_order(root: TreeNode):
    """
        In-order Traversal: LeftChild -> Parent -> RightChild
    """
    left_child = root.get_left()
    right_child = root.get_right()
    if left_child:
        recursive_tree_traversal_dfs_in_order(left_child)
    print(root.value, end=",")
    if right_child:
        recursive_tree_traversal_dfs_in_order(right_child)


def recursive_tree_traversal_dfs_pre_order(root: TreeNode):
    """
        Pre-Order Traversal: Root -> Left-child -> Right-child
    """
    left_child = root.get_left()
    right_child = root.get_right()
    print(root.value, end=",")
    if left_child:
        recursive_tree_traversal_dfs_pre_order(left_child)
    if right_child:
        recursive_tree_traversal_dfs_pre_order(right_child)


def recursive_tree_traversal_dfs_post_order(root: TreeNode):
    """
        Post-order Traversal: Left-child -> Right-child -> Root
    """
    left_child = root.get_left()
    right_child = root.get_right()
    if left_child:
        recursive_tree_traversal_dfs_post_order(left_child)
    if right_child:
        recursive_tree_traversal_dfs_post_order(right_child)
    print(root.value, end=",")


if __name__ == '__main__':
    root = create_binary_tree()
    print("in-order: ", end="")
    recursive_tree_traversal_dfs_in_order(root)     # in-order: 4,2,8,5,1,6,9,3,7,
    print()

    print("pre-order: ", end="")
    recursive_tree_traversal_dfs_pre_order(root)
    print()

    print("post-order: ", end="")
    recursive_tree_traversal_dfs_post_order(root)


