"""
You are given an empty AVL tree. You need to insert N integer keys into it, one by one, maintaining the AVL property after each insertion.

Your task is to implement the insert function that inserts a key into the AVL tree and rebalances it if required.

After all insertions, print the preorder traversal of the final AVL tree.

Input Format

The first line contains an integer N, the number of nodes to insert.

The second line contains N space-separated integers representing the keys to insert sequentially.

Constraints

1 ≤ N ≤ 1000 1 ≤ Key ≤ 10^5 Keys are unique.

Output Format

Print the preorder traversal of the final balanced AVL tree (space-separated).

Sample Input 0

3
30 20 10

Sample Output 0

20 10 30

Explanation 0

Insert 30, 20, 10 Tree becomes unbalanced at node 30 (Left-Left case)

Perform Right Rotation Final tree: 20 / \ 10 30

Preorder: 20 10 30

Sample Input 1

3
10 30 20

Sample Output 1

20 10 30

Explanation 1

Insert 10, 30, 20

Tree becomes unbalanced at node 10 (Right-Left case)

Perform Right Rotation on (30) then Left Rotation on (10) Final balanced tree: 20 / \ 10 30
"""
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, root, key):
        # Step 1: Perform normal BST insertion
        if not root:
            return TreeNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # Step 2: Update height of current node
        self.update_height(root)
        
        # Step 3: Get balance factor
        balance = self.get_balance(root)
        
        # Step 4: Rebalance if needed
        
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def insert_key(self, key):
        self.root = self.insert(self.root, key)
    
    def preorder_traversal(self, root):
        if root:
            result = [str(root.key)]
            result.extend(self.preorder_traversal(root.left))
            result.extend(self.preorder_traversal(root.right))
            return result
        return []

def main():
    n = int(input().strip())
    keys = list(map(int, input().strip().split()))
    
    avl = AVLTree()
    
    for key in keys:
        avl.insert_key(key)
    
    preorder = avl.preorder_traversal(avl.root)
    print(" ".join(preorder))

if __name__ == "__main__":
    main()