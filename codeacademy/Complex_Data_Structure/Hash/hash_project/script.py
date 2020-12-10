class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head = head_node

    def insert(self, new_node):
        current_node = self.head

        if not current_node:
            self.head = new_node

        while(current_node):
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self):
        str_list = ""
        current_node = self.head
        while(current_node):
            str_list += str(current_node.get_value()) + " "
            current_node = current_node.get_next_node()
        return str_list


node1 = Node("hello")
node2 = Node("hi")
node3 = Node("good-bye")
l1 = LinkedList()
l1.insert(node1)
l1.insert(node2)
l1.insert(node3)
print(l1.__iter__())
