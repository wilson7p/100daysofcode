#Write a program to implement a binary tree and perform tree traversal (inorder, preorder, postorder).
print ("\nWilson - Day 53 of #100DaysOfCode\n") 
print("\nprogram to implement a binary tree and perform tree traversal (inorder, preorder, postorder)\n")

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)
def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("inorder Traversal:")
inorder_traversal(root)
print("preorder Traversal:")
preorder_traversal(root)
print("postorder Traversal:")
postorder_traversal(root)
