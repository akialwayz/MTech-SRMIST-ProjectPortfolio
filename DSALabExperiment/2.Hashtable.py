class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        return key % self.MAX

    def insert(self, key):
        index = self.get_hash(key)
        if self.arr[index] is None:
            self.arr[index] = key
        else:
            # linear probing
            i = 1
            while self.arr[(index+i)%self.MAX] is not None:
                i += 1
            self.arr[(index+i)%self.MAX] = key

t = HashTable()
t.insert(7)
t.insert(18)
t.insert(41)
t.insert(94)
print(t.arr)
