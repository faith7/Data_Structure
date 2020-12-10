class HashMap:
    def __init__(self, array_size=0):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]

    def hash(self, key, num_collisions=0):
        encoded = key.encode()
        hash_code = sum(encoded)
        return hash_code + num_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        current_index = self.compressor(self.hash(key))
        current_array_value = self.array[current_index]

        if current_array_value is None:
            self.array[current_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[current_index] = [key, value]
            return

        else:
            num_collisions = 1

        while(current_array_value[0] != key):
            new_index = self.compressor(self.hash(key, num_collisions))
            new_array_value = self.array[new_index]

            if new_array_value is None:
                self.array[new_index] = [key, value]
                return

            if new_array_value[0] == key:
                self.array[new_index][1] = value
                return
            num_collisions += 1

        return print("inserted successfully", self.array)

    def retrieve(self, key):
        return_index = self.compressor(self.hash(key))
        return_array_value = self.array[return_index]

        if return_array_value is None:
            return None

        if return_array_value[0] == key:
            return return_array_value[1]

        else:
            num_collisions = 1

        while(return_array_value[0] != key):
            new_index = self.compressor(self.hash(key, num_collisions))
            new_array_value = self.array[new_index]

            if new_array_value is None:
                return None

            if new_array_value[0] == key:
                return new_array_value[1]
            else:
                num_collisions += 1
        return


# HashMap testing
hash1 = HashMap(10)
# print(hash1.hash('hello'))
# print(hash1.compressor(532))
hash1.assign('hello', 'world')
hash1.assign('hi', 'stranger')
hash1.assign('good bye', 'myfriend')
print(hash1.retrieve('hello'))
print(hash1.retrieve('good bye'))
print(hash1.retrieve('hi'))
