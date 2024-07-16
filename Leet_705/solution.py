class MyHashSet:
    """
    Design a HashSet without using any built-in hash table libraries.

    Implement MyHashSet class:
    """
    def __init__(self):
        self.table: dict[int, bool] = {}

    def add(self, key: int) -> None:
        self.table[key] = True
        
    def remove(self, key: int) -> None:
        if key in self.table:
            self.table[key] = False
        
    def contains(self, key: int) -> bool:
        if key in self.table:
            return self.table[key]

        return False


def main() -> None:
    hashset = MyHashSet()

    hashset.add(1)
    hashset.add(2)
    print(f"Conatins 1? {hashset.contains(1)}")
    print(f"Conatins 3? {hashset.contains(3)}")
    hashset.add(2)
    print(f"Conatins 2? {hashset.contains(2)}")
    print(hashset.table)
    hashset.remove(2)
    hashset.remove(100)
    print(f"Conatins 2? {hashset.contains(2)}")
    print(hashset.table)


if __name__ == "__main__":
    main()