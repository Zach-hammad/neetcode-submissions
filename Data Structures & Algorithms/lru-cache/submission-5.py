class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_end(key)
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.lru:
            self.lru.move_to_end(key)
        self.lru[key] = value
        if len(self.lru) > self.capacity:
            self.lru.popitem(last=False)
