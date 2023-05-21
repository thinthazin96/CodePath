'''
235. Lowest Common Ancestor of a Binary Search Tree

Time Complexity: O(log n) - n is the number of nodes in the tree
Space Complexity: O(1) - constant space is used
'''
def lowestCommonAncestor(root, p, q):
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
        

