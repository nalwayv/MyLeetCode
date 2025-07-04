class MinStack:
    def __init__(self):
        self.values: list[tuple[int, int]] = []

    def is_empty(self) -> bool:
        return len(self.values) == 0
    
    def push(self, val: int) -> None:
        if self.is_empty():
            self.values.append((val, val))
        else:
            self.values.append((val, min(val, self.values[-1][1])))

    def pop(self) -> None:
        if self.is_empty():
            return
        self.values.pop()

    def top(self) -> int:
        if self.is_empty():
            return -1
    
        return self.values[-1][0]

    def getMin(self) -> int:
        if self.is_empty():
            return -1

        return self.values[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def main() -> None:
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(f"GetMin: {ms.getMin()} == -3")
    ms.pop()
    print(f"Top: {ms.top()} == 0")
    print(f"GetMin: {ms.getMin()} == -2")

if __name__ == "__main__":
    main()