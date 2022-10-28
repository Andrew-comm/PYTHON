 
class Hash_Table:
    def __init__(self) :
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(key):
       h = 0
       for char in key:
          h += ord(char)
       return h % 100
    
    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

t = Hash_Table
print(t.add("march 6",130))