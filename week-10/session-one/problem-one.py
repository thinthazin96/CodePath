'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3] 
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

Edge case:
What if the tree is empty?
what if there is one node in the tree?

Match: Preorder is the most suitable algorithm for this case

1) Recursively traverse the tree using Pre-Order traversal
    a) If the nodes from both trees are not None, and their values are equal -> Recur on their children
    b) Else -> return False
2) After trees have been fully traversed and no differences are discovered, return True

Time Complexity: O(N), where N is the number of nodes in both trees
Space Complexity: O(NlogN) for balanced tree, O(N) for unbalanced tree (space is used for the recursion stack)
'''
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):

    if not p and not q: 
        return True

    if not p or not q: #if one of them is empty, return False
        return False

    if p.val != q.val: #if the value of the tree is different, return False
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def main():
    tests = [
    {
        'input' : (Node(1), Node(1)),
        'output' : True
    },
    {
        'input' : (None , None),
        'output' : True
    },
    {
        'input' : (None , Node(1)),
        'output' : False
    },
    {
        'input' : (Node(1) , None),
        'output' : False
    },
    {
        'input' : (Node(1, Node(2), Node(3)) , Node(1, Node(2), Node(3))),
        'output' : True
    },
    {
        'input' : (Node(1, Node(2)) , Node(1, Node(2))),
        'output' : True
    },
    {
        'input' : (
            Node(1, None, Node(3)), 
            Node(1, None, Node(3))),
        'output' : True
    },
        {
        'input' : (
            Node(1, Node(2)), 
            Node(1, None, Node(3))),
        'output' : False
    },
    {
        'input' : (
            Node(1, Node(2), Node(3)) , 
            Node(1, Node(2), Node(4))),
        'output' : False
    },
    ]
    for i in range(len(tests)):
        print(f'Test {i+1} Pass:', is_same_tree(*tests[i]['input']) == tests[i]['output'])

main()


