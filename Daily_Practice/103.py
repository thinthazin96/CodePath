'''
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Time Complexity: O(n)
'''
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    '''
    Recursive:
    1. base case: if root is empty, return 0.
    2. if the root is not null, return 1 + max(left, right). 
    (1 is for the root node)
    '''
    if not root:
        return 0
    return 1 + max(zigzagLevelOrder(root.left), zigzagLevelOrder(root.right))


def zigzagLevelOrderBFS(root):
    '''
    iterative bfs: level order traversal using queue
    1. Base case: if root is empty, return 0.
    2. create a queue and append the root node.
    3. while the queue is not empty, pop the first element and append its left and right child to the queue.
    4. return the level.
    '''
    if not root:
        return 0
    queue = [root]
    level = 0
    while queue:
        level += 1
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return level

def zigzagLevelOrderDFS(root):
    '''
    iterative dfs: level order traversal using stack
    1. Base case: if root is empty, return 0.
    2. create a stack and append the root node.
    3. while the stack is not empty, pop the first element and append its left and right child to the stack.
    4. return the level.
    '''
    if not root:
        return 0
    stack = [root] #[3] -> [9, 20] -> [20] -> [15, 7] -> [7] -> []
    level = 0       #1  ->  2              ->  3
    while stack:
        level += 1
        for i in range(len(stack)):
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return level



#how to create tree nodes
root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
# print(zigzagLevelOrder(root))
# print(zigzagLevelOrderBFS(root))
print(zigzagLevelOrderDFS(root))