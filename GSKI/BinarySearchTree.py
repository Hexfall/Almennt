class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class Node():
    def __init__(self, key, data, left = None, right = None, prev = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.prev = prev

class MyComparableKey():
    def __init__(self, int_value, string_value):
        self.int = int_value
        self.str = string_value

    def __str__(self):
        return "({}, {})".format(self.int, self.str)
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return self.int == other.int and self.str == other.str
    
    def __lt__(self, other):
        if self.int > other.int:
            return False
        if self.int == other.int:
            return self.str < other.str
        return True
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return not self <= other
    
    def __ge__(self, other):
        return not self < other

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
                if node.right == None:
                    node.right = Node(key, data, prev = node)
                    break
                node = node.right
            else:
                if node.left == None:
                    node.left = Node(key, data, prev = node)
                    break
                node = node.left
    
    def update(self, key, data):
        node = self.get_node(key)
        node.data = data
    
    def get_node(self, key):
        node = self.tree
        while node != None:
            if node.key == key:
                return node
            elif node.key < key:
                node = node.right
            else:
                node = node.left
        raise NotFoundException()
    
    def find(self, key):
        return self.get_node(key).data
    
    def contains(self, key):
        try:
            self.get_node(key)
            return True
        except:
            return False
    
    def remove(self, key):
        def get_side_node(tree):
            if tree.left != None:
                return get_right(tree.left)
            return get_left(tree.right)
        def get_left(tree):
            if tree.left == None:
                return tree
            return get_left(tree.left)
        def get_right(tree):
            if tree.right == None:
                return tree
            return get_right(tree.right)

        node = self.get_node(key)
        if node.prev == None and node.left == None and node.right == None:
            self.tree = None
        elif node.right == None and node.left == None:
            prev = node.prev
            if prev.right is node:
                prev.right = None
            else:
                prev.left = None
        else:
            side = get_side_node(node)
            node.data = side.data
            node.key = side.key
            parent = side.prev
            if parent.left is side:
                parent.left = side.right
            else:
                parent.right = side.left        

    def __str__(self):
        def preorder(tree):
            if tree == None:
                return ""
            left, right = preorder(tree.left), preorder(tree.right)
            return " ".join([i for i in [str(tree.data), left, right] if i != ""])
        def inorder(tree):
            if tree == None:
                return None
            left, right = inorder(tree.left), inorder(tree.right)
            return " ".join([i for i in [left, str(tree.data), right] if i != None])
        def postorder(tree):
            if tree == None:
                return ""
            left, right = postorder(tree.left), postorder(tree.right)
            return " ".join([i for i in [left, right, str(tree.data)] if i != ""])
        
        return "\n".join([preorder(self.tree), inorder(self.tree), postorder(self.tree)])
        
    def __repr__(self):
        return str(self)
    
    def __getitem__(self, key):
        return self.find(key)
    
    def __setitem__(self, key, data):
        try:
            self.insert(key, data)
        except:
            self.update(key, data)
    
    def __len__(self):
        def size(tree):
            if tree == None:
                return 0
            return 1 + size(tree.left) + size(tree.right)
        return size(self.tree)

a = BSTMap()
a.insert(5, 5)
a.insert(3, 3)
a.insert(4, 4)
a.insert(2, 2)
a.insert(6, 6)
print(a)
a.update(6, 7)
print(len(a))
print(a)
a.remove(5)
print(a)