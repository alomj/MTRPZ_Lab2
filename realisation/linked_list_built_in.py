import time


class ArrayLinkedList:
    def __init__(self):
        self._items = []

    def length(self) -> int:
        return len(self._items)

    def _validate_index(self, index: int, allow_insert: bool = False) -> None:
        if allow_insert:
            if index < 0 or index > self.length():
                raise IndexError("Wrong index provided")
        else:
            if index < 0 or index >= self.length():
                raise IndexError("Wrong index provided")

    def append(self, element: str) -> None:
        if not element:
            raise TypeError("Cannot add an empty element")
        self._items.append(element)

    def insert(self, element: str, index: int) -> None:
        self._validate_index(index, allow_insert=True)
        self._items.insert(index, element)

    def delete(self, index: int) -> str:
        self._validate_index(index)
        return self._items.pop(index)

    def delete_all(self, element: str) -> None:
        self._items = [el for el in self._items if el != element]

    def get(self, index: int) -> str:
        self._validate_index(index)
        return self._items[index]

    def clone(self) -> "ArrayLinkedList":
        new_obj = ArrayLinkedList()
        new_obj._items = self._items.copy()
        return new_obj

    def reverse(self) -> None:
        self._items.reverse()

    def find_first_element(self, element: str) -> int:
        if element not in self._items:
            return -1
        return self._items.index(element)

    def find_last_element(self, element: str) -> int:
        for i in range(self.length() - 1, -1, -1):
            if self._items[i] == element:
                return i
        return -1

    def clear(self) -> None:
        self._items = []

    def extend(self, other: "ArrayLinkedList") -> None:
        self._items.extend(other._items.copy())


if __name__ == "__main__":
    ll = ArrayLinkedList()
    print(f'Initial list: has {ll.length()} elements')

    for char in 'ABCDEFG':
        ll.append(char)
        print(f'After adding {char} to list: its length is {ll.length()} elements')
        time.sleep(0.1)

    ll.insert('X', 0)
    print(f'After adding X to list at index 0 we have: {ll.get(0)} and current length is {ll.length()} elements')
    time.sleep(0.1)

    removed = ll.delete(1)
    print(f'After removing element at index 1 (expected A), removed value: {removed}')
    time.sleep(0.1)

    ll.append('A')
    print(f'Appended another A. Current list length: {ll.length()}')
    time.sleep(0.1)

    ll.delete_all('A')
    print(f'After deleting all A elements, first index of A is: {ll.find_first_element("A")}')
    time.sleep(0.1)

    clone = ll.clone()
    print(f'Cloned list. Clone length: {clone.length()} | Original length: {ll.length()}')
    time.sleep(0.1)

    clone.delete(0)
    print(f'After deleting first element from clone: clone length = {clone.length()}, original length = {ll.length()}')
    time.sleep(0.1)

    ll.reverse()
    print(f'After reversing the original list, element at index 0 is now: {ll.get(0)}')
    time.sleep(0.1)

    print(f"First index of 'C' in original list: {ll.find_first_element('C')}")
    time.sleep(0.1)
    print(f"Last index of 'C' in original list: {ll.find_last_element('C')}")
    time.sleep(0.1)

    ll.clear()
    print(f'After clearing the original list, length is now: {ll.length()}')
    time.sleep(0.1)

    list1 = ArrayLinkedList()
    list1.append('X')
    list1.append('Y')
    list2 = ArrayLinkedList()
    list2.append('Z')
    list1.extend(list2)
    print(f'After extending list1 with list2: list1 length = {list1.length()}')
    print(f'Contents of list1 after extend: {list1._items}')