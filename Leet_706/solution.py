class MyHashMap:
    """
    Implement the MyHashMap class
    """
    def __init__(self):
        self.table: dict[int, int] = {}

    def put(self, key: int, value: int) -> None:
        self.table[key] = value
        
    def remove(self, key: int) -> None:
        if key in self.table:
            del self.table[key]
    
    def get(self, key: int) -> int:
        if key in self.table:
            return self.table[key]
        return -1
    

def main() -> None:
    hashmap = MyHashMap()

    hashmap.put(1, 1)
    hashmap.put(2, 2)
    print(f"Get 1? {hashmap.get(1)}")
    print(f"Get 3? {hashmap.get(3)}")
    hashmap.put(2, 1)
    print(f"Get 2? {hashmap.get(2)}")
    hashmap.remove(2)
    print(f"Get 2? {hashmap.get(2)}")

    
if __name__ == "__main__":
    main()