# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 12:14:29 2025

@author: suresh.burra
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    """Insert a value into BST"""
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

def inorder_traversal(root, result):
    """Perform in-order traversal and store result"""
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)

def main():
    # Read input
    n = int(input().strip())
    nodes = list(map(int, input().strip().split()))
    
    # Construct BST
    root = None
    for val in nodes:
        root = insert_into_bst(root, val)
    
    # Perform in-order traversal
    result = []
    inorder_traversal(root, result)
    
    # Print result
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()