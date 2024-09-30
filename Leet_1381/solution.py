class CustomStack:
    def __init__(self, maxSize: int):
        self._stk: list[int] = []
        self._max_size: int = maxSize

    def _is_full(self) -> bool:
        return len(self._stk) == self._max_size
    
    def _is_empty(self) -> bool:
        return not self._stk

    def push(self, x: int) -> None:
        if self._is_full():
            return
        self._stk.append(x)
        
    def pop(self) -> int:
        if self._is_empty():
            return -1
        
        return self._stk.pop()
        
    def increment(self, k: int, val: int) -> None:
        if self._is_empty():
            return
        n: int = len(self._stk)
        for i in range(k):
            if i < n:
                self._stk[i] += val


def main() -> None:
    print("1381. Design a Stack With Increment Operation")

    stk = CustomStack(3)
    
    stk.push(1)
    stk.push(2)
    stk.pop()
    stk.push(2)
    stk.push(3)
    stk.push(4)
    stk.increment(5,100)
    stk.increment(2,100)
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()


if __name__ == "__main__":
    main()