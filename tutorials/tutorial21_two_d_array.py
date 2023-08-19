if __name__ == '__main__':
    """
    Do NOT use multiplication to create 1D or 2D arrays in Python as it creates unexpected behaviors like:
        arr = [0] * 10
    This creates an array of length 10, but all of them point to the same int obj due to multiplication
    
    See: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/ 
    """

    # Use list COMPREHENSION
    arr = [0 for i in range(5)]     # [0, 0, 0, 0, 0]
    print(arr)

    # For 2D array, use nested loop in list comprehension
    row, col = 3, 4     # This is more like a tuple assignment

    # This is how to create a 2D array in Java
    # for(int r...) {
    #    for(int c...) {
    #       a[r][c] = 0;
    #    }
    # }

    arr = [[0 for c in range(col)] for r in range(row)]
    print(arr)      # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    # Traditional code with type declaration like in Java
    # The syntax->      var-name: type = initialized-value
    # Note that though we declare the var-type, later we can still assign another-type-value to that var
    # E.g:      x: int = 10
    #           x = "Hello"
    arr: list[list[int]] = []
    for r in range(row):
        new_row: list[int] = []
        for c in range(col):
            new_row.append(0)
        arr.append(new_row)

    print(arr)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

