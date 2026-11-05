class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor(value) {
    const newNode = new Node(value);
    this.head = newNode;
    this.tail = newNode;
    this.length = 1;
  }

  printList() {
    let temp = this.head;
    while (temp !== null) {
      console.log(temp.value);
      temp = temp.next;
    }
  }

  append(value) {
    const newNode = new Node(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length += 1;
    return true;
  }

  pop() {
    if (this.length === 0) return null;
    let temp = this.head;
    let pre = this.head;
    while (temp.next) {
      pre = temp;
      temp = temp.next;
    }
    this.tail = pre;
    this.tail.next = null;
    this.length -= 1;
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return temp;
  }

  prepend(value) {
    const newNode = new Node(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length += 1;
    return true;
  }

  popFirst() {
    if (this.length === 0) return null;
    const temp = this.head;
    this.head = this.head.next;
    temp.next = null;
    this.length -= 1;
    if (this.length === 0) {
      this.tail = null;
    }
    return temp;
  }

  get(index) {
    if (index < 0 || index >= this.length) return null;
    let temp = this.head;
    for (let i = 0; i < index; i++) {
      temp = temp.next;
    }
    return temp;
  }

  setValue(index, value) {
    const temp = this.get(index);
    if (temp) {
      temp.value = value;
      return true;
    }
    return false;
  }

  insert(index, value) {
    if (index < 0 || index > this.length) return false;
    if (index === 0) return this.prepend(value);
    if (index === this.length) return this.append(value);
    const newNode = new Node(value);
    const temp = this.get(index - 1);
    newNode.next = temp.next;
    temp.next = newNode;
    this.length += 1;
    return true;
  }

  remove(index) {
    if (index < 0 || index >= this.length) return null;
    if (index === 0) return this.popFirst();
    if (index === this.length - 1) return this.pop();
    const prev = this.get(index - 1);
    const temp = prev.next;
    prev.next = temp.next;
    temp.next = null;
    this.length -= 1;
    return temp;
  }

  reverse() {
    let temp = this.head;
    this.head = this.tail;
    this.tail = temp;
    let after = null;
    let before = null;
    for (let i = 0; i < this.length; i++) {
      after = temp.next;
      temp.next = before;
      before = temp;
      temp = after;
    }
  }
}

// ---------------- Examples ----------------
const ll = new LinkedList(1);
console.log("init:");
ll.printList(); // 1

// append: add to the end -> O(1)
ll.append(2);
ll.append(3);
console.log("append 2, 3:");
ll.printList(); // 1 2 3

// prepend: add to the front -> O(1)
ll.prepend(0);
console.log("prepend 0:");
ll.printList(); // 0 1 2 3

// pop: remove and return the last node -> O(n)
console.log("pop:", ll.pop().value); // 3
ll.printList(); // 0 1 2

// popFirst: remove and return the first node -> O(1)
console.log("popFirst:", ll.popFirst().value); // 0
ll.printList(); // 1 2

// get: return the node at an index -> O(n)
console.log("get(1):", ll.get(1).value); // 2
console.log("get(10):", ll.get(10)); // null

// setValue: overwrite the value at an index
console.log("setValue(1, 20):", ll.setValue(1, 20)); // true
console.log("setValue(10, 99):", ll.setValue(10, 99)); // false
ll.printList(); // 1 20

// insert: put a new node at an index (0 = front, length = end)
ll.insert(0, 5); // 5 1 20
ll.insert(2, 10); // 5 1 10 20
ll.insert(4, 30); // 5 1 10 20 30
console.log("insert 5@0, 10@2, 30@4:");
ll.printList(); // 5 1 10 20 30
console.log("insert(99, 1):", ll.insert(99, 1)); // false

// remove: delete the node at an index and return it
console.log("remove(0):", ll.remove(0).value); // 5
console.log("remove(1):", ll.remove(1).value); // 10
console.log("remove(2):", ll.remove(2).value); // 30
console.log("remove(99):", ll.remove(99)); // null
ll.printList(); // 1 20

// reverse: flip the list in place -> O(n)
ll.append(300);
console.log("before reverse:");
ll.printList(); // 1 20 300
ll.reverse();
console.log("after reverse:");
ll.printList(); // 300 20 1
console.log("head:", ll.head.value, "tail:", ll.tail.value, "length:", ll.length); // 300 1 3

