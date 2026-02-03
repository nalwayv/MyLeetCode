from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: dict[int, int] = {}
        self.order: deque[int] = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.order.remove(key)
        self.order.appendleft(key)
        return self.cache[key]

    def remove(self) -> None:
        if len(self.cache) == self.cap:
            self.cache.pop(self.order.pop())

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.appendleft(key)
        else:
            self.remove()
            self.cache[key] = value
            self.order.appendleft(key)


def main() -> None:
    print('146. LRU Cache')

    lru = LRUCache(2)
    lru.put(1,1)
    lru.put(2,2)
    print(lru.get(1))
    lru.put(3,3)
    print(lru.get(2))
    lru.put(4,4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))


if __name__ == '__main__':
    main()