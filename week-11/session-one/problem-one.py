class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def is_same_tree(p, q):
  if not p and not q: return True
  if not p or not q: return False
  if p.val != q.val: return False
  return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right) 

def insert_in_bst(root, val):
    if not root:
        return Node(val)
    
    if val > root.val:                                 #if the val is greater than the root, go to right
        root.right = insert_in_bst(root.right, val)    #recurs all the way to the right leaf
    else:                                               #if the tree is less than the root value, go to left
        root.left = insert_in_bst(root.left, val)       #recurs all the way to the left leaf

    return root
def main():
  tests = [
    {
      'input': {
        'root': None,
        'val': 1
      },
      'output': Node(1)
    },
    {
      'input': {
        'root': Node(2),
        'val': 1
      },
      'output': Node(2, Node(1))
    },
    {
      'input': {
        'root': Node(2),
        'val': 3
      },
      'output': Node(2, None, Node(3))
    },
    {
      'input': {
        'root': Node(3, Node(1), Node(5)),
        'val': 2
      },
      'output': Node(3, Node(1, None, Node(2)), Node(5))
    },
    {
      'input': {
        'root': Node(3, Node(1), Node(5)),
        'val': 4
      },
      'output': Node(3, Node(1), Node(5, Node(4)))
    },
    {
      'input': {
        'root': Node(4, Node(2, Node(1), Node(3)), Node(7)),
        'val': 5
      },
      'output': Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5)))
    },
    {
      'input': {
        'root': Node(40, Node(20, Node(10), Node(30)), Node(60, Node(50), Node(70))),
        'val': 25
      },
      'output': Node(40, Node(20, Node(10), Node(30, Node(25))), Node(60, Node(50), Node(70)))
    },
  ]

  for i in range(len(tests)):
    print(f'Test {i+1} Pass:', is_same_tree(insert_in_bst(tests[i]['input']['root'], tests[i]['input']['val']), tests[i]['output']))

main()