class FrontMiddleBackQueue:
    def __init__(self):
        self._queue: list[int] = []
        
    def pushFront(self, val: int) -> None:
        """
        Inserts value at the front of the queue.

        Args:
            val (int): The value to insert at the front of the queue.
        """
        if not self._queue:
            self.pushBack(val)
        else:
            self._queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        """
        Inserts value into the middle of the queue.

        Args:
            val (int): The value to insert into the middle of the queue.
        """
        if not self._queue:
            self.pushBack(val)
        else:
            mid: int = len(self._queue) // 2
            self._queue.insert(mid, val)

    def pushBack(self, val: int) -> None:
        """
        Inserts value to the back of the queue.

        Args:
            val (int): The value to insert into the back of the queue.
        """
        self._queue.append(val)        

    def popFront(self) -> int:
        """
        Removes and returns the element from the front of the queue.
        
        Returns:
            int: The value at the front of the queue, or -1 if the queue is empty.
        """
        if not self._queue:
            return -1
        
        return self._queue.pop(0)

    def popMiddle(self) -> int:
        """
        Removes and returns the element from the middle of the queue.

        Returns:
            int: The value from the middle of the queue, or -1 if the queue is empty.
        """
        if not self._queue:
            return -1
        
        mid: int = (len(self._queue) - 1) // 2
        return self._queue.pop(mid)

    def popBack(self) -> int:
        """
        Removes and returns the element from the back of the queue.

        Returns:
            int: The value from the back of the queue, or -1 if the queue is empty.
        """
        if not self._queue:
            return -1
        
        return self._queue.pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()


def main() -> None:
    print("1670. Design Front Middle Back Queue")

    que = FrontMiddleBackQueue()
    que.pushFront(1)
    que.pushBack(2)
    que.pushMiddle(3)
    que.pushMiddle(4)

    print(f"PopFront equals 1? {"pass" if que.popFront() == 1 else "fail"}")
    print(f"popMiddle equals 3? {"pass" if que.popMiddle() == 3 else "fail"}")
    print(f"popMiddle equals 4? {"pass" if que.popMiddle() == 4 else "fail"}")
    print(f"popBack equals 2? {"pass" if que.popBack() == 2 else "fail"}")
    print(f"popFront equals -1? {"pass" if que.popFront() == -1 else "fail"}")


if __name__ == "__main__":
    main()