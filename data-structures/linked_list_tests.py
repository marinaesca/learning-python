# bradyz code, using for tests
# adding in my own code, making test cases

'''
Implement the required functions in linked_list.py,
then run "python linked_list_tests.py".
'''

import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    def test_to_string(self):
        ll = LinkedList()

        self.assertEqual(str(ll), "")

    def test_add_values(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)

        self.assertEqual(str(ll), "1->2->3")

    def test_add_values_two(self):
        ll = LinkedList()

        ll.add(3)
        ll.add(6)
        ll.add(1)
        ll.add(9)
        ll.add(9)
        ll.add(8)

        self.assertEqual(str(ll), "3->6->1->9->9->8")

    def test_contains_value(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)

        self.assertTrue(ll.contains(1))
        self.assertTrue(ll.contains(2))
        self.assertTrue(ll.contains(3))

        self.assertFalse(ll.contains(10))

    def test_contains_value_two(self):
        ll = LinkedList()

        ll.add(37)
        ll.add(944)
        ll.add(2000)

        self.assertTrue(ll.contains(37))
        self.assertTrue(ll.contains(944))
        self.assertTrue(ll.contains(2000))

        self.assertFalse(ll.contains(1))
        self.assertFalse(ll.contains(38))
        self.assertFalse(ll.contains(20))

    def test_remove_value(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)

        self.assertEqual(str(ll), "1->2->3")

        ll.remove(2)

        self.assertEqual(str(ll), "1->3")

    def test_remove_value_two(self):
        ll = LinkedList()

        ll.add(70)
        ll.add(80)
        ll.add(90)
        ll.add(900)
        ll.add(800)
        ll.add(700)

        self.assertEqual(str(ll), "70->80->90->900->800->700")

        ll.remove(90)

        self.assertEqual(str(ll), "70->80->900->800->700")

        ll.remove(900)

        self.assertEqual(str(ll), "70->80->800->700")

    def test_remove_value_head(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)

        self.assertEqual(str(ll), "1->2->3")

        ll.remove(1)

        self.assertEqual(str(ll), "2->3")

    def test_remove_value_mult(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.add(1)
        ll.add(1)

        self.assertEqual(str(ll), "1->2->3->1->1")

        ll.remove(1)

        self.assertEqual(str(ll), "2->3->1->1")

    def test_remove_value_all(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.add(1)
        ll.add(1)

        self.assertEqual(str(ll), "1->2->3->1->1")

        ll.removeAll(1)

        self.assertEqual(str(ll), "2->3")     


if __name__ == "__main__":
    unittest.main()