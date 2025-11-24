# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 13:15:57 2025

@author: suresh.burra
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    """Insert a value into BST maintaining BST properties"""
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

def delete_node(root, key):
    """Delete a node with given key from BST while maintaining BST properties"""
    if root is None:
        return root
    
    # Search for the node to be deleted
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Node to be deleted found
        
        # Case 1: Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Case 2: Node with two children
        # Get the inorder successor (smallest in the right subtree)
        temp = find_min(root.right)
        
        # Copy the inorder successor's value to this node
        root.val = temp.val
        
        # Delete the inorder successor
        root.right = delete_node(root.right, temp.val)
    
    return root

def find_min(node):
    """Find the node with minimum value in a BST"""
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorder_traversal(root):
    """Return in-order traversal as list"""
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    
    traverse(root)
    return result

def main():
    # Read input
    n = int(input().strip())
    nodes = list(map(int, input().strip().split()))
    k = int(input().strip())
    
    # Construct BST
    root = None
    for val in nodes:
        root = insert_into_bst(root, val)
    
    # Delete node K if it exists
    root = delete_node(root, k)
    
    # Print in-order traversal after deletion
    result = inorder_traversal(root)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()