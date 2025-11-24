# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 12:32:27 2025

@author: suresh.burra
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

def postorder_traversal(root, result):
    """Post-order: Left → Right → Root"""
    if root:
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.val)

# For the coding problem format (post-order instead of in-order)
def main():
    n = int(input().strip())
    nodes = list(map(int, input().strip().split()))
    
    root = None
    for val in nodes:
        root = insert_into_bst(root, val)
    
    result = []
    postorder_traversal(root, result)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
    
    