import heapq

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.height = None
    
    def AddNeighbor(self, other):
        self.neighbors.add(other)
        other.neighbors.add(self)
    
    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.height == other.height

    def __gt__(self, other):
        return self.height > other.height

    def __geq__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return self.height < other.height

    def __leq__(self, other):
        return not self > other

m, n = [int(i) for i in input().split()]
nodes = []
for y in range(m):
    nodes.append([Node(int(i)) for i in input().split()])
for y in range(m):
    for x in range(n):
        if y != m - 1:
            nodes[y][x].AddNeighbor(nodes[y+1][x])
        if x != n - 1:
            nodes[y][x].AddNeighbor(nodes[y][x+1])
nodes[0][0].height = 0
target = nodes[m - 1][n - 1]
cands = []
heapq.heappush(nodes[0][0])
while True:
    curnode = heapq.heappop(cands)
    if curnode == target:
        break
    for nei in curnode.neighbors:
        if nei.height == None:
            nei.height = max(nei.val - curnode.val, curnode.height)
        else:
            nei.height = min(nei.height, max(nei.val - curnode.val, curnode.height))
        nei.neighbors.remove(curnode)
        heapq.heappush(cands, nei)
print(target.height)