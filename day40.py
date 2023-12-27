#To find the minimum value in a Binary Search Tree (BST)
print("\nWilson - Day 40 of #100DaysOfCode\n")
print("\nBinary Search Tree")

class TreeNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

def find_min_value(root):
  while root.left is not None:
    root = root.left
  return root.key

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

min_value = find_min_value(root)
print("minimum value of binary search tree is: ", min_value)
