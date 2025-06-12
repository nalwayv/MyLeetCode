from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.frequency: dict[int, int] = {}
        self.stack: dict[int, list[int]] = defaultdict(list)
        self.top: int = -1

    def push(self, val: int) -> None:
        self.frequency[val] = self.frequency.get(val, 0) + 1
        self.top = max(self.top, self.frequency[val])
        self.stack[self.frequency[val]].append(val)

    def pop(self) -> int:
        if arr := self.stack.get(self.top):
            pop: int = arr.pop()
            self.frequency[pop] -= 1

            if not arr:
                self.top -= 1

            return pop

        return -1


def main() -> None:
    print("895. Maximum Frequency Stack")

    fs = FreqStack()

    fs.push(5) # The stack is [5]
    fs.push(7) # The stack is [5,7]
    fs.push(5) # The stack is [5,7,5]
    fs.push(7) # The stack is [5,7,5,7]
    fs.push(4) # The stack is [5,7,5,7,4]
    fs.push(5) # The stack is [5,7,5,7,4,5]

    print(fs.pop()) # 5
    print(fs.pop()) # 7
    print(fs.pop()) # 5
    print(fs.pop()) # 4
    print(fs.pop()) # 7
    print(fs.pop()) # 5


if __name__ == "__main__":
    main()