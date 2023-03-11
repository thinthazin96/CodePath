"""
1448. Count Good Nodes in Binary Tree

Time Complexity: O(n) run the tree 1 time 
Space Complexity: O(height of tree) 

"""
class Tree:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    '''
    DFS Preorder
    1) Create helper fucntion to go deep and track maxVal and count for "good" nodes.
    2) Base case: if the node == empty, return 0
    3) if node.val >= maxVal, set the count to 1, otherwise, 0.
    4) Update maxVal by find maximum between current node val and maxVal.
    5) Update count by count + helper fun(node.left, maxVal)
    6) do the same for right side.
    7) return the res
    '''
    def dfs(node, maxVal):
        if not node:    #base case if the node is empty.
            return 0
        
        if node.val >= maxVal: #found good node
            good_count = 1
        else:
            good_count = 0
        
        maxVal = max(node.val, maxVal)      #update max value in visited path
        good_count += dfs(node.left, maxVal) #Update good_count by recursive on left subtree
        good_count += dfs(node.right, maxVal) #Update good_count by recursive on right subtree
        return good_count   #Return the number of Good node
        
    return dfs(root, root.val) 

print(goodNodes(Tree(3,Tree(1, Tree(3, None, None), None), Tree(4, Tree(1, None, None), Tree(5, None, None)))))

        
