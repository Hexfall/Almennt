class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def palindrome(head, cur = 0):
    def get_size(node):
        if node == None:
            return 0
        return 1 + get_size(node.next)
    def get_node(node, nr = 0):
        if nr <= 0 or node == None:
            return node
        return get_node(node.next, nr - 1)
    size = get_size(head)
    if size == 0 or size == 1 or size // 2 < cur:
        return True
    if get_node(head, cur).data == get_node(head, size - 1 - cur).data:
        return palindrome(head, cur + 1)
    return False

if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")