class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity
        self.size = 0
        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        
        #value = self.cache[key]
        #del self.cache[key]
        self.cache.move_to_end(key)
        #self.cache[key] = value
        #print(self.cache)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if self.size >= self.cap:
                self.cache.popitem(0)
                self.size -= 1
            self.cache[key] = value
            self.size += 1
        
        #print(self.cache)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)