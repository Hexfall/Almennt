class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class Node():
    def __init__(self, key, data, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BSTMap():
    def __init__(self):
        self.tree = None
    
    def insert(self, key, data):
        if self.tree == None:
            self.tree = Node(key, data)
            return
        node = self.tree
        while True:
            if node.key == key:
                raise ItemExistsException()
            elif node.key < key:
                if node.left == None:
                    node.left = Node(key, data)
                    break
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(key, data)
                    break
                node = node.right
    
    def update(self, key, data):
        node = self.tree
        while True:
            if node == None:
                raise NotFoundException()
            elif node.key == key:
                node.data = data
                break
            elif node.key < key:
                node = node.left
            else:
                node = node.right

    def __str__(self):
        def preorder(tree):
            if tree == None:
                return ""
            left, right = preorder(tree.left), preorder(tree.right)
            return " ".join([i for i in [str(tree.data), left, right] if i != ""])
        def inorder(tree):
            if tree == None:
                return ""
            left, right = inorder(tree.left), inorder(tree.right)
            return " ".join([i for i in [left, str(tree.data), right] if i != ""])
        def postorder(tree):
            if tree == None:
                return ""
            left, right = postorder(tree.left), postorder(tree.right)
            return " ".join([i for i in [left, right, str(tree.data)] if i != ""])
        
        return "\n".join([preorder(self.tree), inorder(self.tree), postorder(self.tree)])
        
    def __repr__(self):
        return str(self)

a = BSTMap()
a.insert(5, 5)
a.insert(3, 3)
a.insert(4, 4)
a.insert(6, 6)
print(a)