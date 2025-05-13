import unittest
from realisation.linked_list_built_in import ArrayLinkedList

class TestArrayLinkedList(unittest.TestCase):
    def test_append_and_length(self):
        ll = ArrayLinkedList()
        self.assertEqual(ll.length(), 0)
        ll.append("A")
        self.assertEqual(ll.length(), 1)
        self.assertEqual(ll.get(0), "A")

    def test_append_empty_element_raises(self):
        ll = ArrayLinkedList()
        with self.assertRaises(TypeError):
            ll.append("")

    def test_insert(self):
        ll = ArrayLinkedList()
        ll.append("A")
        ll.insert("B", 0)
        self.assertEqual(ll.get(0), "B")
        self.assertEqual(ll.get(1), "A")

    def test_insert_invalid_index(self):
        ll = ArrayLinkedList()
        with self.assertRaises(IndexError):
            ll.insert("X", 1)

    def test_delete(self):
        ll = ArrayLinkedList()
        ll.append("A")
        result = ll.delete(0)
        self.assertEqual(result, "A")
        self.assertEqual(ll.length(), 0)

    def test_delete_invalid_index(self):
        ll = ArrayLinkedList()
        with self.assertRaises(IndexError):
            ll.delete(0)

    def test_delete_all(self):
        ll = ArrayLinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("A")
        ll.delete_all("A")
        self.assertEqual(ll.length(), 1)
        self.assertEqual(ll.get(0), "B")

    def test_clone(self):
        ll = ArrayLinkedList()
        ll.append("A")
        clone = ll.clone()
        self.assertEqual(clone.length(), 1)
        self.assertEqual(clone.get(0), "A")
        clone.append("B")
        self.assertEqual(ll.length(), 1)

    def test_reverse(self):
        ll = ArrayLinkedList()
        ll.append("A")
        ll.append("B")
        ll.reverse()
        self.assertEqual(ll.get(0), "B")
        self.assertEqual(ll.get(1), "A")

    def test_find_first_element(self):
        ll = ArrayLinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("A")
        self.assertEqual(ll.find_first_element("A"), 0)
        self.assertEqual(ll.find_first_element("B"), 1)
        self.assertEqual(ll.find_first_element("X"), -1)

    def test_find_last_element(self):
        ll = ArrayLinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("A")
        self.assertEqual(ll.find_last_element("A"), 2)
        self.assertEqual(ll.find_last_element("B"), 1)
        self.assertEqual(ll.find_last_element("X"), -1)

    def test_clear(self):
        ll = ArrayLinkedList()
        ll.append("A")
        ll.clear()
        self.assertEqual(ll.length(), 0)

    def test_extend(self):
        list1 = ArrayLinkedList()
        list1.append("A")
        list2 = ArrayLinkedList()
        list2.append("B")
        list1.extend(list2)
        self.assertEqual(list1.length(), 2)
        self.assertEqual(list1.get(1), "B")
        self.assertEqual(list2.length(), 1)

    def test_get_invalid_index(self):
        ll = ArrayLinkedList()
        with self.assertRaises(IndexError):
            ll.get(0)


if __name__ == "__main__":
    unittest.main()