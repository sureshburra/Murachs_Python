#-------------------------------------------------------------------------------
# Name:        Kruskals Algorithm
# Purpose:
#
# Author:      suresh.burra
#
# Created:     23-11-2025
# Copyright:   (c) suresh.burra 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False  # They are already in same set → cycle

        # Union by Rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True

def kruskal(n, edges):

    edges.sort()  # Step 1: Sort edges by weight (ascending)

    dsu = DSU(n)
    mst = []
    total_weight = 0

    for w, u, v in edges:
        if dsu.union(u, v):  # Step 2: Add edge only if no cycle
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight

