class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.index = 0

    def append(self, item):
        if len(self.ring) < self.capacity:
            self.ring.append(item)
        else:
            # replaces the oldest value in the ring
            self.ring[self.index] = item
            self.index += 1
            # resets the index once it exceeds the capacity
            if self.index + 1 > self.capacity:
                self.index = 0

    def get(self):
        return [i for i in self.ring if i is not None]

# Tests from Readme

# buffer = RingBuffer(3)

# print(buffer.capacity)

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# print(buffer.get())

# buffer.append('d')

# print(buffer.get())

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())
