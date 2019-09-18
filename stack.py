class Stack:
    def __init__(self):
        self.items = list()

    def is_empty(self):
            return not self.items

    def push(self,data):
        self.items.append(data)
        return True

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return False
        popped_item = self.items.pop()
        return popped_item

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            #print("The stack is:")
            for i in self.items:
                print(i, end = " ")
            print("\n")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return False
        return self.items[-1]



if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(3)
    my_stack.push(6)
    my_stack.print_stack()
    my_stack.push(4)
    my_stack.print_stack()
    print(f"\nThe popped value is:{my_stack.pop()}")
    my_stack.print_stack()






