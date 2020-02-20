class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def Add(self, data):
        if self.next == None:
            self.next = Node(data)
        else:
            self.next.Add(data)
    
    def __str__(self):
        if self.next == None:
            return str(self.data)
        return " ".join([str(self.data), str(self.next)])
    
    def __len__(self):
        if self.next == None:
            return 1
        return 1 + len(self.next)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def Add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head.Add(data)
        
    def Pop(self):
        if self.head == None:
            return None
        toRet = self.head.data
        self.head = self.head.next
        return toRet
    
    def HeadToTail(self):
        data = self.Pop()
        self.Add(data)

    def __IndexOfNode(self, node):
        try:
            return node.data.index
        except:
            return -1
    
    def RemoveIndex(self, index):
        def RemoveRec(node, index):
            if node == None or node.next == None:
                return
            if self.__IndexOfNode(node.next) == index:
                node.next = node.next.next
            else:
                RemoveRec(node.next, index)

        if self.__IndexOfNode(self.head) == index:
            self.Pop()
        else:
            RemoveRec(self.head, index)

    def ContainsIndex(self, index):
        def ContainsRec(node, index):
            if node == None:
                return False
            if self.__IndexOfNode(node) == index:
                return True
            return ContainsRec(node.next, index)

        return ContainsRec(self.head, index)
    
    def GetList(self):
        def ListRec(node):
            if node == None:
                return []
            return [node.data] + ListRec(node.next)
        
        return ListRec(self.head)

    def __str__(self):
        if self.head == None:
            return ""
        return str(self.head)
    
    def __repr__(self):
        return str(self)

    def __len__(self):
        if self.head == None:
            return 0
        return len(self.head)