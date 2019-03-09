
class DataClass:
    # USE THIS IMPLEMENTATION OF DATACLASS UNCHANGED
    def __init__(self, x_type, x_information):
        self.x_type = x_type
        self.x_information = x_information
    def __str__(self):
        return "{" + str(self.x_type) + ": " + str(self.x_information) + "}"

class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

class DLL_Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

class DataList:
    def __init__(self):
        self.__list = None
        self.__back_node = None

    def add_to_front(self, value):
        if self.__list == None:
            self.__list = DLL_Node(value)
            self.__back_node = self.__list
        else:
            self.__list.prev = DLL_Node(value, None, self.__list)
            self.__list = self.__list.prev
            #self.__list = DLL_Node(value, next=self.__list)
            #node2 = self.__list.next
            #node2.prev = self.__list

    def add_to_back(self, value):
        if self.__list == None:
            self.__list = DLL_Node(value)
            self.__back_node = self.__list
        else:
            self.__back_node.next = DLL_Node(value, self.__back_node)
            self.__back_node = self.__back_node.next
    
    def get_all_of_type(self, type, remove = False):
        DLWith = DataList()
        DLWout = DataList()
        node = self.__list
        while node != None:
            data = node.data
            if data.x_type == type:
                DLWith.add_to_back(data)
            else:
                DLWout.add_to_back(data)
            node = node.next
        if remove:
            self.__list = DLWout.__list
            self.__back_node = DLWout.__back_node
        return DLWith

    def __str__(self):
        def get_str(head):
            if head == None:
                return ""
            return str(head.data) + " " + get_str(head.next)
        return get_str(self.__list)

def count_value(head, value):
    if head == None:
        return 0
    if head.data == value:
        return 1 + count_value(head.next, value)
    return count_value(head.next, value)

def contains_all(head1, head2):
    def contains(head, value):
        if head == None:
            return False
        if head.data == value:
            return True
        return contains(head.next, value)
    if head1 == None:
        return True
    if contains(head2, head1.data):
        return contains_all(head1.next, head2)
    return False

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("\nTesting get_all_of_type")
    dl1 = DataList()
    dl1.add_to_back(DataClass(1, "I: type 1"))
    dl1.add_to_back(DataClass(2, "O: type 2"))
    dl1.add_to_back(DataClass(3, "type 3 DataClass"))
    dl1.add_to_back(DataClass(1, "Other type 1"))
    dl1.add_to_back(DataClass(2, "More info: type 2"))
    dl1.add_to_back(DataClass(1, "Type 1 D.C."))
    print("dl1: " + str(dl1))
    dl2 = dl1.get_all_of_type(2)
    print("dl2: " + str(dl2))
    print("dl1: " + str(dl1))
    dl3 = dl1.get_all_of_type(1, True)
    print("dl3: " + str(dl3))
    print("dl1: " + str(dl1))