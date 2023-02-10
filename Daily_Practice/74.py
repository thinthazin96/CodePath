'''
74. Search a 2D Matrix

Time Complexity: log(m * n)
'''
def searchMatrix(matrix, target):
    Rows = len(matrix)
    Cols = len(matrix[0])

    top, bot = 0, Rows - 1
    while top < bot:
        row = (top + bot) // 2

        if target < matrix[row][-1]:
            bot = row - 1
        elif target > matrix[row][0]:
            top = row + 1
        else:
            break

    row = (top + bot) // 2
    l, r = 0, Cols - 1
    while l < r:
        m = (l + r) // 2
        if target < matrix[row][m]:
            l = m + 1
        elif target > matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


