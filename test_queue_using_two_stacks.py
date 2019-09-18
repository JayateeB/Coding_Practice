import unittest
from queue_using_two_stacks import MyQueue


class TestEnqueue(unittest.TestCase):

    def test_rear_after_push(self):
        queue = MyQueue()
        queue.enqueue(3)
        self.assertEqual(queue.queue_rear(),3)
        queue.enqueue(4)
        self.assertEqual(queue.queue_rear(), 4)
        queue.enqueue(5)
        queue.enqueue(6)
        self.assertEqual(queue.queue_rear(), 6)

    def test_dequeued_value(self):
        queue = MyQueue()
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)

    def test_front_after_dequeue(self):
        queue = MyQueue()
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        queue.dequeue()
        self.assertEqual(queue.queue_front(), 4)
        queue.dequeue()
        self.assertEqual(queue.queue_front(), 5)





