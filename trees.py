class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def insert(self, val):
        if val < self.val:
            if self.left == None:
                self.left == val
            else:
                self.insert(self.left, val)
        elif val > self.val:
            if self.right == None:
                self.right == val
            else:
                self.insert(self.left, val)
    

def print_tree(root):
    print_tree(root.left)
    if root != None:
        print(root.val)
    print_tree(root.right)  

vals = [3,9,2,34,76, 23, 93]
root = Node(50)
for i in vals:
    root.insert(i)

print_tree(root)