class Node:
    def __init__(self, key = None, data = None, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "({}) {} ({})".format(str(self.left), str(self.data), str(self.right))

    def __repr__(self):
        return self.__str__()

class TreeClass:
    def __init__(self, preset = 0):
        self.tree = None
        if preset == 1:
            self.tree = Node(5, 5, Node(2, 2, Node(1, 1), Node(4, 4)), Node(8, 8, Node(7, 7), Node(9, 9)))
        elif preset == 2:
            self.tree = Node(3, "c", Node(1, "a", None, Node(2, "b")), Node(5, "e", Node(4, "d"), Node(6, "f")))
        elif preset == 3:
            self.tree = Node(20, 20, Node(13, 13, Node(8, 8), Node(15, 15)), Node(27, 27, Node(21, 21)))
    
    def __str__(self):
        def preorder(tree):
            if tree == None:
                return None
            if tree.left == None and tree.right == None:
                return str(tree.data)
            elif tree.left == None:
                return str(tree.data) + " " + preorder(tree.right)
            elif tree.right == None:
                return str(tree.data) + " " + preorder(tree.left)
            return str(tree.data) + " " + preorder(tree.left) + " " + preorder(tree.right)

        def postorder(tree):
            if tree == None:
                return None
            if tree.left == None and tree.right == None:
                return str(tree.data)
            elif tree.left == None:
                return postorder(tree.right) + " " + str(tree.data)
            elif tree.right == None:
                return postorder(tree.left) + " " + str(tree.data)
            return postorder(tree.left) + " " + postorder(tree.right) + " " + str(tree.data)

        def inorder(tree):
            if tree == None:
                return None
            if tree.left == None and tree.right == None:
                return str(tree.data)
            elif tree.left == None:
                return str(tree.data) + " " + inorder(tree.right)
            elif tree.right == None:
                return inorder(tree.left) + " " + str(tree.data)
            return inorder(tree.left) + " " + str(tree.data) + " " + inorder(tree.right)

        return "\n".join([preorder(self.tree), inorder(self.tree), postorder(self.tree)])

    def insert(self, key, data):
        def setkey(tree, key, data):
            if tree.key == key:
                tree.data = data
            elif tree.key > key:
                if tree.left == None:
                    tree.left = Node(key, data)
                else:
                    setkey(tree.left, key, data)
            else:
                if tree.right == None:
                    tree.right = Node(key, data)
                else:
                    setkey(tree.right, key, data)

        if self.tree:
            setkey(self.tree, key, data)
        else:
            self.tree = Node(key, data)

    def get(self, key):
        def get(tree, key):
            if tree == None:
                return None
            elif tree.key == key:
                return tree.data
            elif tree.key > key:
                return get(tree.left, key)
            return get(tree.right, key)
        
        return get(self.tree, key)

    def __setitem__(self, key, data):
        self.insert(key, data)

    def __getitem__(self, key):
        return self.get(key)

class Bucket:
    def __init__(self, key, data, next = None):
        self.key = key
        self.data = data
        self.next = next

class HashClass:
    def __init__(self, preset = 0):
        self.buckets = [None for _ in range(16)]
        self.size = 16

    def insert(self, key, data):
        def setitem(head, key, data):
            if head.key == key:
                head.data = data
            elif head.next == None:
                head.next = Bucket(key, data)
            else:
                setitem(head.next, key, data)

        if self.buckets[hash(key)%16] == None:
            self.buckets[hash(key)%16] = Bucket(key, data)
        else:
            setitem(self.buckets[hash(key)%16], key, data)

    def get(self, key):
        def get(head, key):
            if head == None:
                return None
            elif head.key == key:
                return head.data
            else:
                return get(head.next, key)

        return get(self.buckets[hash(key)&16], key)
    
    def __setitem__(self, key, data):
        self.insert(key, data)

    def __getitem__(self, key):
        return self.get(key)
    
    def __str__(self):
        s = ""
        for i in range(len(self.buckets)):
            s += "Bucket {}: ".format(i + 1)
            node = self.buckets[i]
            while node != None:
                s += str(node.data) + " "
                node = node.next
            s += "\n"
        return s
    
    def __repr__(self):
        return self.__str__()


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    h = HashClass()
    h = HashClass(1)

    t = TreeClass()
    t = TreeClass(1)