from nodes import Node


class Stack:
    def __init__(self, limit=100):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return (self.size == 0)

    def pop(self):
        if not (self.is_empty()):
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("you are popping {}".format(self.top_item.get_value())
            return self.top_item.get_value()
        return print("your stack is empty")

    def peek(self):
        if not (self.is_empty()):
            return self.top_item.get_value()
        return print("your stack is empty")

    def push(self, value):
        if self.has_space():
            item=Node(self)
            item.set_next_node(self.top_item)
            self.top_item=item
            self.size += 1
            print("Adding {} node in the stack".format(value))
        else:
            print("Out of space. You cannot push more than \
                the specified limit:{}".format(
                self.limit))


stack1=Stack(5)
stack1.push("bread#1")
stack1.push("bread#2")
stack1.push("bread#3")
stack1.push("bread#4")
stack1.push("bread#5")

stack1.pop()
