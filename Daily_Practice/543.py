'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Time Complexity: 
'''
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    '''
    1. Base Case: if the root is empty, return 0.
    2. Calculate the left and right subtree diameter.
    3. Calculate the left and right subtree height.
    4. Return the max of the left and right subtree diameter and the sum of left and right subtree height.
    '''
    if not root:
        return 0
    left_diameter = diameterOfBinaryTree(root.left) #go as long as root has left child
    right_diameter = diameterOfBinaryTree(root.right) # go as long as root has right child
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_diameter, right_diameter, left_height + right_height)

def height(root):
    '''
    1. Base Case: if the root is empty, return 0.
    2. Return 1 + max(left, right) height.
    '''
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))     



#create a tree
root = TreeNode(1, None, None)  #1  
root.left = TreeNode(2, None, None) #2
root.right = TreeNode(3, None, None) #3
root.left.left = TreeNode(4, None, None) #4
root.left.right = TreeNode(5, None, None) #5
root.right.left = TreeNode(6, None, None) #6

print(diameterOfBinaryTree(root))