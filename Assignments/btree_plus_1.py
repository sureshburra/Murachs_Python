# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 11:13:10 2025

@author: suresh.burra
"""

class Node:
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf
        self.next = None

class BPlusTree:
    def __init__(self):
        self.root = Node(is_leaf=True)
    
    def insert(self, key, value):
        print(f"Inserting {key} -> {value}")
        result = self._insert(self.root, key, value)
        if result is not None:
            # Root was split, create new root
            new_root = Node()
            new_root.keys = [result['key']]
            new_root.children = [result['left'], result['right']]
            self.root = new_root
        self.display_tree()
        
    
    def _insert(self, node, key, value):
        if node.is_leaf:
            return self._insert_into_leaf(node, key, value)
        else:
            # Find the appropriate child
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            
            result = self._insert(node.children[i], key, value)
            
            if result is not None:
                # Child was split, insert the promoted key
                return self._insert_into_internal(node, result['key'], result['left'], result['right'])
        return None
    
    def _insert_into_leaf(self, node, key, value):
        # Find position to insert
        pos = 0
        while pos < len(node.keys) and node.keys[pos] < key:
            pos += 1
        
        node.keys.insert(pos, key)
        node.children.insert(pos, value)
        
        # Check if we need to split (max 1 key for order 2)
        if len(node.keys) > 1:
            return self._split_leaf(node)
        return None
    
    def _insert_into_internal(self, node, key, left_child, right_child):
        # Find position to insert
        pos = 0
        while pos < len(node.keys) and node.keys[pos] < key:
            pos += 1
        
        node.keys.insert(pos, key)
        node.children[pos] = left_child
        node.children.insert(pos + 1, right_child)
        
        # Check if we need to split (max 1 key for order 2)
        if len(node.keys) > 1:
            return self._split_internal(node)
        return None
    
    def _split_leaf(self, node):
        # For order 2, split into two nodes with 1 key each
        new_node = Node(is_leaf=True)
        
        # Move the second key to new node
        new_node.keys = [node.keys[1]]
        new_node.children = [node.children[1]]
        
        # Keep first key in original node
        node.keys = [node.keys[0]]
        node.children = [node.children[0]]
        
        # Link leaves
        new_node.next = node.next
        node.next = new_node
        
        # Return the split result (promote first key of new node)
        return {
            'key': new_node.keys[0],
            'left': node,
            'right': new_node
        }
    
    def _split_internal(self, node):
        # For order 2, split internal node
        new_node = Node(is_leaf=False)
        
        if len(node.keys) == 2:
            # Case: [key1, key2] -> promote key2, keep key1 in left, right gets empty
            promoted_key = node.keys[1]
            new_node.keys = []
            new_node.children = [node.children[2]]
            
            node.keys = [node.keys[0]]
            node.children = [node.children[0], node.children[1]]
        else:
            # General case (shouldn't occur for order 2)
            mid = len(node.keys) // 2
            promoted_key = node.keys[mid]
            
            new_node.keys = node.keys[mid+1:]
            new_node.children = node.children[mid+1:]
            
            node.keys = node.keys[:mid]
            node.children = node.children[:mid+1]
        
        return {
            'key': promoted_key,
            'left': node,
            'right': new_node
        }
    
    def display_tree(self):
        if not self.root:
            return
        
        levels = []
        queue = [(self.root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if level >= len(levels):
                levels.append([])
            
            node_type = "Leaf" if node.is_leaf else "Internal"
            levels[level].append((node_type, node.keys.copy()))
            
            if not node.is_leaf:
                for child in node.children:
                    queue.append((child, level + 1))
        
        # Print levels with exact formatting
        for i, level_nodes in enumerate(levels):
            print(f"Level {i}: ", end="")
            nodes_str = []
            for node_type, keys in level_nodes:
                nodes_str.append(f"{node_type}({keys})")
            print(" | ".join(nodes_str), end=" | \n")

# Test the implementation
if __name__ == "__main__":
    tree = BPlusTree()
    
    tree.insert(5, "a")
    tree.insert(15, "b")
    tree.insert(25, "c")