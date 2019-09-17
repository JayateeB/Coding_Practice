class SetOfStacks:

    MAX_STACK_LENGTH = 2

    def __init__(self):
        self.list_of_stacks = list()

    @staticmethod
    def is_full(stack):
        if len(stack) == SetOfStacks.MAX_STACK_LENGTH:
            return True
        else:
            return False

    def push(self, data):
        if self.list_of_stacks:
            last_stack = self.list_of_stacks[-1]
        if not self.list_of_stacks or SetOfStacks.is_full(last_stack):
            new_stack = list()
            new_stack.append(data)
            self.list_of_stacks.append(new_stack)
        else:
            self.list_of_stacks[-1].append(data)

    def pop(self):
        if not self.list_of_stacks:
            raise ValueError("Cannot Pop from Empty Stack")
        else:
            popped_value = self.list_of_stacks[-1].pop()
            if not self.list_of_stacks[-1]:
                self.list_of_stacks.pop()
        return popped_value

    def display(self):
        print(self.list_of_stacks)

    def peek(self):
        if not self.list_of_stacks:
            print("List is Empty")
            return False
        return self.list_of_stacks[-1][-1]


if __name__ == '__main__':
    new_set_of_stacks = SetOfStacks()

    new_set_of_stacks.push(1)
    new_set_of_stacks.push(2)
    new_set_of_stacks.push(3)
    new_set_of_stacks.push(4)
    new_set_of_stacks.push(5)
    print(f"Popped value: {new_set_of_stacks.pop()}")
    new_set_of_stacks.display()








