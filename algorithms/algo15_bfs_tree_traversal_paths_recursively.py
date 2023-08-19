from collections import deque

from algorithms.algo11_binary_tree import TreeNode

from algorithms.algo11_binary_tree import create_binary_tree


def get_path_of_a_binary_tree_recursively_wrapper1(root: TreeNode):
    """
        This is a wrapper for users to use, this function doesn't return anything since the function it calls inside
        will print out all the paths
    """
    path: list[TreeNode] = [root]
    # Here we don't need to return anything, just basically call the func get_path_of_a_binary_tree_recursively()
    # since this function print all the value out for every single step
    get_path_of_a_binary_tree_recursively1(root, path)


def get_path_of_a_binary_tree_recursively1(root: TreeNode, curr_path: list[TreeNode]):
    left_child = root.get_left()
    right_child = root.get_right()

    if not left_child and not right_child:
        for i in range(len(curr_path)):
            if i == len(curr_path) - 1:
                print(curr_path[i].value)
            else:
                print(curr_path[i].value, end=",")
    if left_child:
        left_list = curr_path.copy()
        left_list.append(left_child)
        get_path_of_a_binary_tree_recursively1(left_child, left_list)
    if right_child:
        right_list = curr_path.copy()
        right_list.append(right_child)
        get_path_of_a_binary_tree_recursively1(right_child, right_list)


def get_path_of_a_binary_tree_recursively2(root: TreeNode, curr_path: list[TreeNode], result_paths: list[list[int]]):
    """
        This time, we don't print out the paths right away, we will return all the results in a list of lists[int]
        Since we need to return result_paths, we just create it once in the wrapper function, and let this function
        modify/append elements into result_paths.
        result_paths is an object, therefore, it is passed by reference. That is, each time this function modifies result_path,
        the function modifies the object itself in the memory, so any changes to result_paths will affect result_paths
        itself.
        This is totally different from primitive vars: they are passed by values. That is, when we pass a primitive var
        to a function, it will have a copy of itself and that copy will be used by the function. Therefore, any changes
        to that var inside the function will not affect their value in the memory

    """
    left_child = root.get_left()
    right_child = root.get_right()

    if not left_child and not right_child:
        # if the node doesn't have any children, we append the current-path into the result list
        nodes_path = []
        for node in curr_path:
            nodes_path.append(node.value)
        result_paths.append(nodes_path)
    if left_child:
        left_list = curr_path.copy()
        left_list.append(left_child)
        get_path_of_a_binary_tree_recursively2(left_child, left_list, result_paths)
    if right_child:
        right_list = curr_path.copy()
        right_list.append(right_child)
        get_path_of_a_binary_tree_recursively2(right_child, right_list, result_paths)


def get_path_of_a_binary_tree_recursively_wrapper2(root: TreeNode) -> list[list[int]]:
    path: list[TreeNode] = [root]
    # We create result_paths here with initialization as an empty list,  we let get_path_of_a_binary_tree_recursively2
    # do the rest of work like how to modify/append elements to result_paths
    result_paths: list[list[int]] = []
    get_path_of_a_binary_tree_recursively2(root, path, result_paths)

    return result_paths


if __name__ == '__main__':
    root = create_binary_tree()
    get_path_of_a_binary_tree_recursively_wrapper1(root)    # 1,2,4
                                                            # 1,2,5,8
                                                            # 1,3,6,9
                                                            # 1,3,7

    print("new paths with return statements:")
    print(get_path_of_a_binary_tree_recursively_wrapper2(root))     # [[1, 2, 4], [1, 2, 5, 8], [1, 3, 6, 9], [1, 3, 7]]
