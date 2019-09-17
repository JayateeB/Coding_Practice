import unittest
from setofstacks import SetOfStacks


class TestPush(unittest.TestCase):

    def test_top_after_push(self):
        stack = SetOfStacks()
        stack.push(3)
        self.assertEquals(stack.peek(),3)
        stack.push(4)
        self.assertEquals(stack.peek(), 4)
        stack.push(5)
        self.assertEquals(stack.peek(), 5)

    def test_popped_value(self):
        stack = SetOfStacks()
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEquals(stack.pop(), 5)
        self.assertEquals(stack.pop(), 4)
        self.assertEquals(stack.pop(), 3)

    def test_top_after_pop(self):
        stack = SetOfStacks()
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.pop()
        self.assertEquals(stack.peek(), 4)
        stack.pop()
        self.assertEquals(stack.peek(), 3)

    def test_pop_from_empty_stack(self):
        stack = SetOfStacks()
        self.assertRaises(ValueError, stack.pop)
        stack.push(3)
        stack.push(4)
        stack.pop()
        stack.pop()
        self.assertRaises(ValueError, stack.pop)

    def test_number_of_stacks(self):
        stack = SetOfStacks()
        stack.push(3)
        self.assertEquals(len(stack.list_of_stacks),(0//SetOfStacks.MAX_STACK_LENGTH) + 1)
        stack.push(4)
        self.assertEquals(len(stack.list_of_stacks), (1 // SetOfStacks.MAX_STACK_LENGTH) + 1)
        stack.push(5)
        self.assertEquals(len(stack.list_of_stacks), (2 // SetOfStacks.MAX_STACK_LENGTH) + 1)
        stack.push(6)
        self.assertEquals(len(stack.list_of_stacks), (3 // SetOfStacks.MAX_STACK_LENGTH) + 1)
        stack.pop()
        self.assertEquals(len(stack.list_of_stacks), (2 // SetOfStacks.MAX_STACK_LENGTH) + 1)









