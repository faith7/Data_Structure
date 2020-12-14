from linkedlist import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for i in range(array_size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assgin(self, key, value):
        array_index = self.compress(self.hash(key))
        # self.array[array_index] = [key, value]
        list_at_index = self.array[array_index]
        payload = Node([key, value])
        for item in list_at_index:
            if item[0] == key:
                item[1] = value
                return
        list_at_index.insert(payload)

    def retrieve(self, key):
        index = self.compress(self.hash(key))
        list_at_index = self.array[index]
        for item in list_at_index:
            if item[0] is not None and item[0] == key:
                return item[1]
        return None


# bloom = HashMap(len(flower_definitions))
# for flower in flower_definitions:
#     bloom.assign(flower[0], flower[1])
# print(bloom.retrieve("daisy"))
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assgin(flower[0], flower[1])
print(blossom.retrieve("daisy"))