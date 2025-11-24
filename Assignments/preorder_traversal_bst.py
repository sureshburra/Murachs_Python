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

def preorder_traversal(root, result):
    """Pre-order: Root → Left → Right"""
    if root:
        result.append(root.val)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)

# For the coding problem format (pre-order instead of in-order)
def main():
    n = int(input().strip())
    nodes = list(map(int, input().strip().split()))
    
    root = None
    for val in nodes:
        root = insert_into_bst(root, val)
    
    result = []
    preorder_traversal(root, result)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()