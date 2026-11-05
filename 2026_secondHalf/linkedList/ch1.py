class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node    
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    

if __name__ == "__main__":
    # __init__: create a list with one node
    ll = LinkedList(1)
    print("init:")
    ll.print_list()              # 1

    # append: add to the end -> O(1)
    ll.append(2)
    ll.append(3)
    print("append 2, 3:")
    ll.print_list()              # 1 2 3

    # prepend: add to the front -> O(1)
    ll.prepend(0)
    print("prepend 0:")
    ll.print_list()              # 0 1 2 3

    # pop: remove and return the last node -> O(n)
    print("pop:", ll.pop().value)  # 3
    ll.print_list()              # 0 1 2

    # pop_first: remove and return the first node -> O(1)
    print("pop_first:", ll.pop_first().value)  # 0
    ll.print_list()              # 1 2

    # get: return the node at an index -> O(n)
    print("get(1):", ll.get(1).value)  # 2
    print("get(10):", ll.get(10))      # None (out of range)

    # set_value: overwrite the value at an index
    print("set_value(1, 20):", ll.set_value(1, 20))  # True
    print("set_value(10, 99):", ll.set_value(10, 99))  # False
    ll.print_list()              # 1 20

    # insert: put a new node at an index (0 = front, length = end)
    ll.insert(0, 5)              # front  -> 5 1 20
    ll.insert(2, 10)             # middle -> 5 1 10 20
    ll.insert(4, 30)             # end    -> 5 1 10 20 30
    print("insert 5@0, 10@2, 30@4:")
    ll.print_list()              # 5 1 10 20 30
    print("insert(99, 1):", ll.insert(99, 1))  # False (invalid index)

    # remove: delete the node at an index and return it
    print("remove(0):", ll.remove(0).value)    # 5   (head)
    print("remove(1):", ll.remove(1).value)    # 10  (middle)
    print("remove(2):", ll.remove(2).value)    # 30  (tail)
    print("remove(99):", ll.remove(99))        # None (invalid index)
    ll.print_list()              # 1 20

    # reverse: flip the list in place -> O(n)
    ll.append(300)
    print("before reverse:")
    ll.print_list()              # 1 20 300
    ll.reverse()
    print("after reverse:")
    ll.print_list()              # 300 20 1
    print("head:", ll.head.value, "tail:", ll.tail.value, "length:", ll.length)  # 300 1 3
