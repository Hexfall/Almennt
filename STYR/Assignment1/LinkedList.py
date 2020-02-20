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
        return " ".join([str(self.data), str(self.next)])

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
    
    def __str__(self):
        if self.head == None:
            return ""
        return str(self.head)