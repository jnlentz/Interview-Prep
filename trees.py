class tree_node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def insert(root, val):
    if root == None: return
    if root.val == val: return
    if val < root.val:
        if root.left != None:
            insert(root.left, val)
        else:
            root.left = tree_node(val)
    elif val > root.val:
        if root.right != None:
            insert(root.right, val)
        else:
            root.right = tree_node(val)
            
           
    

def print_tree(root):
    if root == None: return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)
    

vals = [3,9,2,34,76, 23, 93]
root = tree_node(50)
for i in vals:
    insert(root, i)

print_tree(root)