from random import randrange

class RandomizedSet:
    def __init__(self):
        self.values: set[int] = set()
    
    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        
        self.values.add(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        
        self.values.remove(val)
        return True

    def getRandom(self) -> int:
        if not self.values:
            return -1
        
        r: int = randrange(0, len(self.values))
        result: int = -1
        for i,v in enumerate(self.values):
            result = v
            if i == r:
                break

        return result

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def main() -> None:
    randomized_set = RandomizedSet()
    print(f"[Insert]: {randomized_set.insert(1)}")
    print(f"[Remove]: {randomized_set.remove(2)}")
    print(f"[Insert]: {randomized_set.insert(2)}")
    print(f"[Random]: {randomized_set.getRandom()}")
    print(f"[Remove]: {randomized_set.remove(1)}")
    print(f"[Insert]: {randomized_set.insert(2)}")
    print(f"[Random]: {randomized_set.getRandom()}")


if __name__ == "__main__":
    main()
    