'''
104. Maximum Depth of Binary Tree

Time Complexity: O(n)
'''
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    '''
    1. Base Case: if the root is empty, return 0.
    2. Return 1 + max(left, right) height.
    '''
    if not root:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return 1 + max(left, right)

# create a tree
root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))  #1
print(maxDepth(root))