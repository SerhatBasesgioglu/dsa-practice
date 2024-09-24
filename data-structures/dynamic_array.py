# NOTE: 1D basic dynamic array implementation, uses static array under the hood.
# NOTE: Written for dsa practice.
class DynamicArray:
    def __init__(self):
        self.data = [None] * 1
        self.size = 0
        self.capacity = 1

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bound")
        return self.data[index]

    # TODO: Implement error checking for remove method
    def remove(self, value):
        index = self.data.index(value)
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1


# WARN: Rest of the code is not relevant for DSA study(Except for the tests).
# TODO: Add dunder methods.


# TEST: Run tests in this area.
arr = DynamicArray()
arr.append(1)
print(arr.capacity)
print(arr)
arr.append(2)
print(arr.capacity)
print(arr)
arr.append(0)
print(arr.capacity)
print(arr)
arr.append(1)
print(arr.capacity)
print(arr)
arr.append(1)
print(arr.capacity)
print(arr)
