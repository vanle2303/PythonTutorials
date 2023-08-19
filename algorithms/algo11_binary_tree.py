class TreeNode:
    """
        This is a binary tree class like in Java, we have a root node with/without its left child and right child
    """

    # we first need to create a constructor of the class
    def __init__(self, value: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        """
            This class takes an int value as its root node, and this root node can either have left or right child
            or both of them or even none of them.
            Therefore, value is a required param and left/right are just optional params.
            To declare an optional param, we have to initialize it with a legal default value. In this case, left is
            TreeNode type, then it should be initialized as None
            To refer to the class as the type of var inside that class, we put the class name in quote like
            this 'TreeNode' or "TreeNode"
        """
        self.value = value
        self.__left = left      # __left and __right are private value
        self.__right = right

    # since __left and __right are private, we use setter and getter to set and get the values of private params
    def set_left(self, left: 'TreeNode'):
        self.__left = left

    def set_right(self, right: 'TreeNode'):
        self.__right = right

    def get_left(self) -> 'TreeNode':
        return self.__left

    def get_right(self) -> 'TreeNode':
        return self.__right


def create_binary_tree():
    # here, we create nodes of TreeNode type
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    # Then set left and right child to the created nodes to make a binary tree
    node1.set_left(node2)
    node1.set_right(node3)
    node2.set_left(node4)
    node2.set_right(node5)
    node3.set_left(node6)
    node3.set_right(node7)
    node5.set_left(node8)
    node6.set_right(node9)

    return node1


