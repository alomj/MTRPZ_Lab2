import unittest
from realisation.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_append_and_length(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.length(), 0)
        dll.append("A")
        self.assertEqual(dll.length(), 1)
        self.assertEqual(dll.get(0), "A")

    def test_append_empty_element_raises(self):
        dll = DoublyLinkedList()
        with self.assertRaises(TypeError):
            dll.append("")

    def test_insert(self):
        dll = DoublyLinkedList()
        dll.append("A")
        dll.insert("B", 0)
        self.assertEqual(dll.get(0), "B")
        self.assertEqual(dll.get(1), "A")

    def test_insert_invalid_index(self):
        dll = DoublyLinkedList()
        with self.assertRaises(IndexError):
            dll.insert("X", 1)

    def test_delete(self):
        dll = DoublyLinkedList()
        dll.append("A")
        result = dll.delete(0)
        self.assertEqual(result, "A")
        self.assertEqual(dll.length(), 0)

    def test_delete_invalid_index(self):
        dll = DoublyLinkedList()
        with self.assertRaises(IndexError):
            dll.delete(0)

    def test_delete_all(self):
        dll = DoublyLinkedList()
        dll.append("A")
        dll.append("B")
        dll.append("A")
        dll.delete_all("A")
        self.assertEqual(dll.length(), 1)
        self.assertEqual(dll.get(0), "B")

    def test_clone(self):
        dll = DoublyLinkedList()
        dll.append("A")
        clone = dll.clone()
        self.assertEqual(clone.length(), 1)
        self.assertEqual(clone.get(0), "A")
        clone.append("B")
        self.assertEqual(dll.length(), 1)

    def test_reverse(self):
        dll = DoublyLinkedList()
        dll.append("A")
        dll.append("B")
        dll.reverse()
        self.assertEqual(dll.get(0), "B")
        self.assertEqual(dll.get(1), "A")

    def test_find_first_element(self):
        dll = DoublyLinkedList()
        dll.append("A")
        dll.append("B")
        dll.append("A")
        self.assertEqual(dll.find_first_element("A"), 0)
        self.assertEqual(dll.find_first_element("B"), 1)
        self.assertEqual(dll.find_first_element("X"), -1)

    def test_find_last_element(self):
        dll = DoublyLinkedList()
        dll.append("A")
        dll.append("B")
        dll.append("A")
        self.assertEqual(dll.find_last_element("A"), 2)
        self.assertEqual(dll.find_last_element("B"), 1)
        self.assertEqual(dll.find_last_element("X"), -1)

    def test_clear(self):
        dll = DoublyLinkedList()
        dll.append("A")
        dll.clear()
        self.assertEqual(dll.length(), 0)

    def test_extend(self):
        list1 = DoublyLinkedList()
        list1.append("A")
        list2 = DoublyLinkedList()
        list2.append("B")
        list1.extend(list2)
        self.assertEqual(list1.length(), 2)
        self.assertEqual(list1.get(1), "B")
        self.assertEqual(list2.length(), 1)

    def test_get_invalid_index(self):
        dll = DoublyLinkedList()
        with self.assertRaises(IndexError):
            dll.get(0)


if __name__ == "__main__":
    unittest.main()