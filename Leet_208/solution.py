class Node:
    def __init__(self) -> None:
        self.children: list[Node|None] = [None] * 26
        self.end: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: Node|None = Node()

    def insert(self, word:str) -> None:
        current: Node|None = self.root

        for c in word:
            if not current:
                return
            
            idx: int = ord(c) - ord('a')
            if current.children[idx] == None:
                current.children[idx] = Node()
            current = current.children[idx]
        
        if current:
            current.end = True

    def search(self, word: str) -> bool:
        current: Node|None = self.root
        
        for c in word:
            if not current:
                return False

            idx: int = ord(c) - ord('a')
            if not current.children[idx]:
                return False
            
            current = current.children[idx]

        return current.end if current else False

    def starts_width(self, prefix: str) -> bool:
        current: Node|None = self.root
        
        for c in prefix:
            if not current:
                return False

            idx: int = ord(c) - ord('a')
            if not current.children[idx]:
                return False
            
            current = current.children[idx]

        return True


def main() -> None:
    print("208. Implement Trie (Prefix Tree)")

    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.starts_width("app"))
    trie.insert("app")
    print(trie.search("app"))
    print("end")


if __name__ == "__main__":
    main()