#find middle node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    ll = LinkedList(1)
    for v in [2, 3, 4, 5]:
        ll.append(v)
    print(ll.find_middle_node().value)  # 3

    ll.append(6)
    print(ll.find_middle_node().value)  # 4 (second middle for even length)