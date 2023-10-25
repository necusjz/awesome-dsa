from collections import OrderedDict


class LRUCache:
    def __init__(self, k):
        self.size = k
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)  # update tail

        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value

        if len(self.cache) > self.size:
            self.cache.popitem(last=False)  # remove head
