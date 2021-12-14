class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        value = -1
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        return value

    def put(self, key: int, value: int):
        if key in self.cache:
            self.get(key)
            self.cache[key] = value
        elif len(self.cache) == self.capacity:
            first_key = list(self.cache.keys())[0]
            self.cache.pop(first_key)
            self.cache[key] = value
        else:
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
lRUCache = LRUCache(2)
# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
print(lRUCache.get(2))
print(lRUCache.put(2,6))
print(lRUCache.get(1))
print(lRUCache.put(1,5))
print(lRUCache.put(1,2))
print(lRUCache.get(1))
print(lRUCache.get(2))
# print(lRUCache.put(1,1))
# print(lRUCache.put(2,2))
# print(lRUCache.cache)
# print(lRUCache.get(1))
# print(lRUCache.cache)
# print(lRUCache.put(3,3))
# print(lRUCache.get(2))
# print(lRUCache.put(4,4))
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))

