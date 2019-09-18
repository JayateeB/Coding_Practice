import unittest
from binary_search_tree import Tree


class TestQueue(unittest.TestCase):

    def test_insert_and_search(self):
        bst = Tree()
        bst.insert(5)
        self.assertEqual(bst.search(5),True)
        bst.insert(15)
        self.assertEqual(bst.search(15), True)
        bst.insert(6)
        bst.insert(7)
        self.assertEqual(bst.search(6), True)
        #self.assertEqual(bst.search(16), False)




