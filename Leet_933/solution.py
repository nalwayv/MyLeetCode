from collections import deque

class RecentCounter:
    def __init__(self) -> None:
        self.que: deque[int] = deque()
        self._length: int = 0
        self._milliseconds: int = 3000

    def _peek(self) -> int:
        return self.que[0]
    
    def _check_request(self, diff: int) -> bool:
        if self._length == 0:
            return False
        return self._peek() < diff
    
    def _enque(self, num: int) -> None:
        self.que.append(num)
        self._length += 1

    def _deque(self) -> None:
        _ = self.que.popleft()
        self._length -= 1

    def ping(self, t: int) -> int:
        self._enque(t)

        diff: int = t - self._milliseconds

        # keep de-queing first while its less then diff
        while self._check_request(diff):
            self._deque()

        return self._length


def main() -> None:
    print("933. Number of Recent Calls")

    rc = RecentCounter()
    pings: list[int] = [1,100,3001,3002]
    result: list[int] = [0]*len(pings)

    for i,val in enumerate(pings):
        result[i] = rc.ping(val)
    
    print(result)


if __name__ == "__main__":
    main()