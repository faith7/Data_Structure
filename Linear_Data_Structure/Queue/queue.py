from node import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        if self.max_size is None:
            return True
        else:
            return self.max_size > self.get_size()

    def enqueue(self, value):
        if self.has_space():
            item = Node(value)
            if self.is_empty():
                self.head = item
                self.tail = item
            else:
                self.tail.set_next_node(item)
                self.tail = item
            self.size += 1
            print("Ordering an item:"+str(item.get_value()))

        else:
            print("Sorry.There is no more space")

    def dequeue(self):
        if not(self.is_empty()):
            item = self.head
            print("Now serving" + str(item.get_value()))
            if self.get_size() == 1:
                self.head=None
                self.tail=None
            else:
                self.head=item.get_next_node()
            return item.get_value()
            self.size -= 1
        else:
            print("Nothing to empty")

    def peek(self):
        if not(self.is_empty()):
            item=self.head
            print("You are looking at "+str(item.get_value()))
            return item.get_value()
        else:
            return print("Sorry, there's nothing left here")

deli_line=Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
