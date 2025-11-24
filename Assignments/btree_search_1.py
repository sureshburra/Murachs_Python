import sys


class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, True)

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            new_root = BTreeNode(self.t, False)
            new_root.children.insert(0, root)
            self.split_child(new_root, 0, root)
            self.root = new_root
            self._insert_non_full(new_root, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self.split_child(node, i, node.children[i])
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def split_child(self, parent, i, child):
        t = self.t
        new_child = BTreeNode(t, child.leaf)
        parent.children.insert(i + 1, new_child)
        parent.keys.insert(i, child.keys[t - 1])
        new_child.keys = child.keys[t : (2 * t - 1)]
        child.keys = child.keys[0 : t - 1]
        if not child.leaf:
            new_child.children = child.children[t : (2 * t)]
            child.children = child.children[0:t]

    def search(self, k, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and k == node.keys[i]:
            return node
        if node.leaf:
            return None
        return self.search(k, node.children[i])

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)


if __name__ == "__main__":
    btree = BTree(t=3)

    insert_data = list(map(int, sys.stdin.readline().split()))
    for val in insert_data:
        btree.insert(val)

    search_queries = list(map(int, sys.stdin.readline().split()))

    for query in search_queries:
        result = btree.search(k=query)
        if result:
            print(f"Found {query}")
        else:
            print(f"Could not find {query}")
