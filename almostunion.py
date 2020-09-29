class Node:
    def __init__(self, id):
        self.parent = None
        self.id = id
        self.sum = id
        self.children = []
        self.weight = 1

    def __repr__(self):
        if self.parent:
            return str(self.parent.id) + ": " + str(self.id)
        return str(self.id)
    
    def SetParent(self, other):
        self.parent = other

    def AddChild(self, child):
        self.children.append(child)
        child.parent = self
        self.sum += child.sum
        self.weight += child.weight
    
    def GetParent(self):
        if self.parent == None:
            return self
        p = self.parent
        while p.parent != None:
            p = p.parent
        return p
    
    def RemoveChild(self, child):
        self.children.remove(child)
        child.parent = None
        self.RemoveWeight(child.sum)
    
    def RemoveWeight(self, sum):
        self.weight -= 1
        self.sum -= sum
        p = self.parent
        while p != None:
            p.weight -= 1
            p.sum -= sum
            p = p.parent
    
    def SwitchWithChild(self):
        if self.children == []:
            return
        child = self.children[0]
        self.children.pop(0)
        child.parent = self.parent

        weight = child.weight
        children = child.children
        sum = child.sum
        child.children = self.children
        child.sum = self.sum
        child.weight = self.weight
        self.children = children
        self.sum = sum
        self.weight = weight
        child.children.append(self)
        for c in child.children:
            c.parent = child
        for c in self.children:
            c.parent = self
        if child.parent != None:
            child.parent.children.remove(self)
            child.parent.children.append(child)
    
    def Unlink(self):
        while self.children != []:
            self.SwitchWithChild()
        if self.parent == None:
            return
        self.weight = 1
        self.sum = self.id
        self.parent.RemoveChild(self)

class UnionTree:
    def __init__(self, size):
        self.arr = [Node(i + 1) for i in range(size)]
        self.size = size
    
    def Union(self, index1, index2):
        node1 = self.arr[index1].GetParent()
        node2 = self.arr[index2].GetParent()
        if node1 is node2:
            return
        if node2.weight > node1.weight:
            temp = node1
            node1 = node2
            node2 = temp
        node1.AddChild(node2)
    
    def Move(self, index1, index2):
        node1 = self.arr[index1]
        node2 = self.arr[index2].GetParent()
        if node1.GetParent() == node2:
            return
        node1.Unlink()
        node2.AddChild(node1)
    
    def GetSum(self, index):
        node = self.arr[index].GetParent()
        return str(node.weight) + " " + str(node.sum)

size, coms = [int(i) for i in input().split()]
u = UnionTree(size)
for _ in range(coms):
    inp = [int(i) - 1 for i in input().split()]
    if inp[0] == 0:
        u.Union(*inp[1:])
    elif inp[0] == 1:
        u.Move(*inp[1:])
    elif inp[0] == 2:
        print(u.GetSum(*inp[1:]))