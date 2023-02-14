'''
226. Invert Binary Tree

Time Complexity:
'''
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    '''
    Use DFS
    1. Base Case: if the root is empty, return None.
    2. Save the left node in temp variable.
    3. Replace left node value with right node value.
    4. Replace the right node value with temp.
    5. recursively do both left and right subtree.
    '''
    if not root:
        return None
    
    temp = root.left
    root.left = root.right
    root.left = temp

    invertTree(root.left)
    invertTree(root.right)
    return root