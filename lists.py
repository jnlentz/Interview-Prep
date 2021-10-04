import random

class list_node:
    def __init__(self, val):
        self.val = val
        self.next = None

def append(head, val):
    if head.next == None:
        head.next = list_node(val)
    else:
        append(head.next, val)

def print_list(head):
    print(head.val)
    if head.next != None:
        print_list(head.next)

nums = range(100)
head = list_node(50)
for i in range(15):
    append(head, random.choice(nums))

print_list(head)