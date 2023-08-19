from algorithms.algo11_binary_tree import TreeNode

from algorithms.algo11_binary_tree import create_binary_tree


def tree_traversal_dfs_stack(root_node: TreeNode):
    """
        dfs stands for Depth first search, like in Java, we traverse a tree in-order, post-order, or pre-order
        Those three are the attributes of depth first search traversal

        Stack: First In Last Out ->>> Append right and pop right. So we just simply use append() and pop() for stack
        In Python, we use list to create a stack
    """
    node_stack: list = [root_node]

    while node_stack:
        node = node_stack.pop()
        print(node.value, end=",")

        left_child = node.get_left()
        right_child = node.get_right()

        if left_child:
            node_stack.append(left_child)
        if right_child:
            node_stack.append(right_child)


def tree_traversal_dfs_pre_order_van_logic(root_node: TreeNode):
    """
        Pre-Order Traversal: Root -> Left-child -> Right-child
    """
    node_stack: list = [root_node]

    while node_stack:
        node = node_stack.pop()
        print(node.value, end=",")

        right_child = node.get_right()
        left_child = node.get_left()

        if right_child:
            node_stack.append(right_child)
        if left_child:
            node_stack.append(left_child)


def iterative_tree_traversal_dfs_in_order(root_node: TreeNode):
    """
        In-order Traversal: LeftChild -> Parent -> RightChild
        The main idea is to use a stack,
            First we push the root node onto the stack.
            Then we do a while loop: as long as the stack is not empty, we pop an element out of it, and then print
            its value, and then push its children back onto the stack
    """

    node_stack: list[TreeNode] = [root_node]
    # processed_stack stores boolean values corresponding to the nodes in node_stack. So this is a parallel stack to the
    # node stack
    # Each boolean value in this stack shows if the corresponding node in the node_stack has had its children pushed
    # onto the stack or not
    # We use boolean values to ensure the in-order traversal since we somtimes need to push a node onto the stack,
    # pop it out, and then push it back again in order to maintain the in-order traversal,
    # then we need a signal when to print it
    # Without boolean stack, we may pop the node twice and process it again, which destroys our desired in-order ofnodes
    # True means we already processed the right and left children of the node and pushed the node back to the node_stack
    # False means we haven't processed the children of the node
    processed_stack: list[bool] = [False]

    while node_stack:
        node = node_stack.pop()
        preprocessed = processed_stack.pop()

        # if the node is preprocessed (corresponding bool val = True)
        # or if the node doesn't have any left/right children
        # we print out the node.value
        if preprocessed or (node.get_right() is None and node.get_left() is None):
            print(node.value, end=",")
        else:
            left_child = node.get_left()
            right_child = node.get_right()

            # Since we're using stack to store the nodes, nodes stack will follow first in last out
            # Therefore, in the stack, we have to append right -> root -> left so that when we use pop(), we'll get
            # our desired order: left->root -> right
            if right_child:
                node_stack.append(right_child)
                processed_stack.append(False)

            node_stack.append(node)
            processed_stack.append(True)

            if left_child:
                node_stack.append(left_child)
                processed_stack.append(False)


def iterative_tree_traversal_dfs_post_order(root_node: TreeNode):
    """
        Post-order Traversal: Left-child -> Right-child -> Root
        This post_order example is the same as the in_order example, we just change the order when appending to the
        node_stack: want: left->right->root
                  append: root->right->left
    """
    node_stack: list = [root_node]
    processed_stack: list[bool] = [False]
    while node_stack:
        node = node_stack.pop()
        preprocessed = processed_stack.pop()

        if preprocessed or (node.get_right() is None and node.get_left() is None):
            print(node.value, end=",")
        else:
            left_child = node.get_left()
            right_child = node.get_right()

            node_stack.append(node)
            processed_stack.append(True)

            if right_child:
                node_stack.append(right_child)
                processed_stack.append(False)

            if left_child:
                node_stack.append(left_child)
                processed_stack.append(False)


def iterative_tree_traversal_dfs_pre_order(root_node: TreeNode):
    """
        Pre-Order Traversal: Root -> Left-child -> Right-child
    """
    node_stack: list = [root_node]
    processed_stack: list[bool] = [False]
    while node_stack:
        node = node_stack.pop()
        preprocessed = processed_stack.pop()

        if preprocessed or (node.get_right() is None and node.get_left() is None):
            print(node.value, end=",")
        else:
            left_child = node.get_left()
            right_child = node.get_right()

            if right_child:
                node_stack.append(right_child)
                processed_stack.append(False)

            if left_child:
                node_stack.append(left_child)
                processed_stack.append(False)

            node_stack.append(node)
            processed_stack.append(True)


if __name__ == '__main__':
    root_node = create_binary_tree()
    tree_traversal_dfs_stack(root_node)  # 1,3,7,6,9,2,5,8,4,
    print()

    print("pre_order: ", end="")
    tree_traversal_dfs_pre_order_van_logic(root_node)  # 1,2,4,5,8,3,6,9,7,
    print()

    print("in-order: ", end="")
    iterative_tree_traversal_dfs_in_order(root_node)    # in-order: 4,2,8,5,1,6,9,3,7,
    print()

    print("post-order: ", end="")
    iterative_tree_traversal_dfs_post_order(root_node)  # post-order: 4,8,5,2,9,6,7,3,1,
    print()

    print("pre_order2: ", end="")
    iterative_tree_traversal_dfs_pre_order(root_node)   # pre_order2: 1,2,4,5,8,3,6,9,7,

