class OrderedStream:
    def __init__(self, n: int):
        self.start: int = 0
        self.values: list[str] = [""] * n

    def insert(self, idKey: int, value: str) -> list[str]:
        if idKey > len(self.values) or idKey <= 0:
            return []
        
        self.values[idKey - 1] = value

        # update end
        end = self.start
        while end < len(self.values) and self.values[end]:
            end += 1

        # update start
        start: int = self.start
        while self.start < len(self.values) and self.values[self.start]:
            self.start += 1

        return self.values[start : end]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


def main() -> None:
    print("1656. Design an Ordered Stream")

    os = OrderedStream(5)
    
    print(os.insert(3, "c"))
    print(os.insert(1, "a"))
    print(os.insert(2, "b"))
    print(os.insert(5, "e"))
    print(os.insert(4, "d"))


if __name__ == "__main__":
    main()