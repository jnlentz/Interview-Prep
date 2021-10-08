import random
class tree_node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def insert(root, val):
    if root is None: return tree_node(val)
    if root.val == val:
        return root
    if root.val > val:
        root.left = insert(root.left, val)
    elif root.val < val:
        root.right = insert(root.right, val)
    return root
    
def print_tree(root):
    if root == None: return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)

def height(root):
    if root is None:
        return 1
    else:
        return 1+max(height(root.right),height(root.left))

def numLeaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    else:
        return numLeaves(root.right)+numLeaves(root.left)
            
           
    


    
nums = range(100)
root = tree_node(50)
for i in range(9):
    val = random.choice(nums)
    insert(root, val)

print_tree(root)
print('s = ', numLeaves(root))