class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def _validate_index(self, index: int, allow_insert: bool = False) -> None:
        if allow_insert:
            if index < 0 or index > self.length():
                raise IndexError("Wrong index provided")
        else:
            if index < 0 or index >= self.length():
                raise IndexError("Wrong index provided")

    def _get_node(self, index: int) -> Node:
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def append(self, element: str) -> None:
        if not element:
            raise TypeError("Cannot add an empty element")
        node = Node(element)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def insert(self, element: str, index: int) -> None:
        self._validate_index(index, allow_insert=True)
        node = Node(element)

        if index == 0:
            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node
            if self.size == 0:
                self.tail = node
        elif index == self.size:
            self.append(element)
            return
        else:
            next_node = self._get_node(index)
            prev_node = next_node.prev
            node.prev = prev_node
            node.next = next_node
            if prev_node:
                prev_node.next = node
            next_node.prev = node
        self.size += 1

    def delete(self, index: int) -> str:
        self._validate_index(index)
        node = self._get_node(index)
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1
        return node.data

    def delete_all(self, element: str) -> None:
        current = self.head
        while current:
            next_node = current.next
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
            current = next_node

    def get(self, index: int) -> str:
        self._validate_index(index)
        return self._get_node(index).data

    def clone(self) -> "DoublyLinkedList":
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self) -> None:
        current = self.head
        self.tail = current
        prev = None
        while current:
            current.prev, current.next = current.next, current.prev
            prev = current
            current = current.prev
        self.head = prev

    def find_first_element(self, element: str) -> int:
        index = 0
        current = self.head
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def find_last_element(self, element: str) -> int:
        index = self.size - 1
        current = self.tail
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def extend(self, other: "DoublyLinkedList") -> None:
        current = other.head
        while current:
            self.append(current.data)
            current = current.next


if __name__ == "__main__":
    dll = DoublyLinkedList()

    print(f"Initial length: {dll.length()}")

    dll.append("A")
    dll.append("B")
    dll.append("C")
    print(f"After appending A, B, C: {dll.length()}")

    dll.insert("X", 1)
    print(f"After inserting X at index 1: {dll.get(1)}")

    print("Current elements:")
    for i in range(dll.length()):
        print(f"Index {i}: {dll.get(i)}")

    dll.delete(2)
    print("After deleting index 2:")
    for i in range(dll.length()):
        print(f"Index {i}: {dll.get(i)}")

    print(f"Find first element 'X': {dll.find_first_element('X')}")
    print(f"Find last element 'X': {dll.find_last_element('X')}")

    dll.reverse()
    print("After reversing:")
    for i in range(dll.length()):
        print(f"Index {i}: {dll.get(i)}")

    clone = dll.clone()
    clone.delete(0)
    print(f"Clone after deleting index 0: {clone.get(0)}")
    print(f"Original still has index 0: {dll.get(0)}")
