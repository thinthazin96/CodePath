'''
100. Same Tree

Time Complexity: O(p+q) size of both tree
'''
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def isSameTree(p, q):
    '''
    1. Recursively traverse the tree using Pre-order 
    1. if p.val not same as q.val, return False.
    2. if both p and q are empty, return True.
    3. if one of p or q is empty, return False.
    5. After tree is fully traversed and no difference is found, return True.
    '''
    if not p and not q: #base case
        return True
    if not p or not q:  
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right,q.right)