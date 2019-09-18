from stack import Stack


class MyQueue:

    def __init__(self):
        self.stack_newest_on_top = Stack()
        self.stack_oldest_on_top = Stack()

    def enqueue(self,data):
        self.stack_newest_on_top.push(data)

    def dequeue(self):
        if self.stack_oldest_on_top.is_empty():
            if not self.stack_newest_on_top.is_empty():
                while not self.stack_newest_on_top.is_empty():
                    self.stack_oldest_on_top.push(self.stack_newest_on_top.pop())
                return self.stack_oldest_on_top.pop()
            else:
                print("Queue is empty")
                return False
        return self.stack_oldest_on_top.pop()

    def print_queue(self):
        if self.stack_oldest_on_top.is_empty() and self.stack_newest_on_top.is_empty():
            print("Queue is empty")
        elif not self.stack_oldest_on_top.is_empty():
            temp_stack_oldest_on_top = self.stack_oldest_on_top
            while not temp_stack_oldest_on_top.is_empty():
                print(temp_stack_oldest_on_top.pop(),end = " ")
        elif not self.stack_newest_on_top.is_empty():
            self.stack_newest_on_top.print_stack()

    def queue_front(self):
        if self.stack_oldest_on_top.is_empty():
            if self.stack_newest_on_top.is_empty():
                print("Queue is empty")
                return False
            else:
                while not self.stack_newest_on_top.is_empty():
                    self.stack_oldest_on_top.push(self.stack_newest_on_top.pop())
                return self.stack_oldest_on_top.peek()
        return self.stack_oldest_on_top.peek()

    def queue_rear(self):
        if self.stack_newest_on_top.is_empty():
            if self.stack_oldest_on_top.is_empty():
                print("Queue is empty")
                return False
            else:
                temp_stack_oldest_on_top = self.stack_oldest_on_top
                while not temp_stack_oldest_on_top.is_empty():
                    value_at_rear = temp_stack_oldest_on_top.pop()
                return value_at_rear
        else:
            return self.stack_newest_on_top.peek()



if __name__ == '__main__':
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.print_queue()
    print(f"The dequeued value is: {queue.dequeue()}")
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(8)
    queue.enqueue(1)
    print(f"The dequeued value is: {queue.dequeue()}")
    print(f"The dequeued value is: {queue.dequeue()}")
    queue.print_queue()



