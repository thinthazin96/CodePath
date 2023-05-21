'''
102. Binary Tree Level Order Traversal

Time Complexity: O(n) - n is the number of nodes in the tree
Space Complexity: O(n/2) - > O(n) - n is the number of elements(nodes of tree) in queue
'''
def levelOrder(root):
    res = []
    q = collections.deque()

    #if the root is not null, add it to the queue
    if root:
        q.append(root)

    #while the queue is not empty
    while q:
        level = []
        for i in range(len(q)):
            #pop the first element from the queue
            node = q.popleft()
            #add the value of the node to the level list
            level.append(node.val)
            #if the node has a left child, add it to the queue
            if node.left:
                q.append(node.left)
            #if the node has a right child, add it to the queue
            if node.right:
                q.append(node.right)
        #add the level list to the res list
        res.append(level)
    return res
 