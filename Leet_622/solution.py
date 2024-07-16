class MyCircularQueue:
    """
    Design Circular Queue
    """
    def __init__(self, k: int):
        self.front: int = -1
        self.rear: int = -1
        self.count: int = 0
        self.capacity: int = k
        self.values: list[int] = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.capacity
        self.values[self.rear] = value
        self.count += 1
        
        # if start of a new que
        if self.front == -1:
            self.front = self.rear
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        self.count -= 1

        return True        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.values[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.values[self.rear]
        
    def isEmpty(self) -> bool:
        return self.front == -1
        
    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front
    
    def print_to_console(self) -> None:
        if self.isEmpty():
            return
        
        start: int = self.front
        i: int = self.count
        print("[Que]: ", end="")
        print("[", end="")
        while i != 0:
            if i == 1:
                print(f"{self.values[start]}", end="")
            else:
                print(f"{self.values[start]},", end="")

            start = (start + 1) % self.capacity
            i -= 1
        print("]")


def test_1() -> None:
    k: int = 3
    que = MyCircularQueue(k)
    print(f"[Enque]: {que.enQueue(1)}") # return True
    print(f"[Enque]: {que.enQueue(2)}") # return True
    print(f"[Enque]: {que.enQueue(3)}") # return True
    print(f"[Deque]: {que.enQueue(4)}") # return False
    print(f"[Rear]: {que.Rear()}")      # return 3
    print(f"[Full]: {que.isFull()}")    # return True
    print(f"[Deque]: {que.deQueue()}")  # return True
    print(f"[Enque]: {que.enQueue(4)}") # return True
    print(f"[Rear]: {que.Rear()}")      # return 4

def test_2() -> None:
    k: int = 3
    que = MyCircularQueue(k)
    que.enQueue(1)
    que.enQueue(2)
    que.enQueue(3)
    que.print_to_console()

    # print(f"[Enque]: {que.enQueue(6)}") # return True
    # print(f"[Rear]: {que.Rear()}")      # return 6
    # print(f"[Rear]: {que.Rear()}")      # return 6
    # print(f"[Deque]: {que.deQueue()}")  # return True
    # print(f"[Enque]: {que.enQueue(5)}") # return True
    # print(f"[Rear]: {que.Rear()}")      # return 5
    # print(f"[Deque]: {que.deQueue()}")  # return True
    # print(f"[Front]: {que.Front()}")    #

def main() -> None:
    print("[Test 1]")
    test_1()
    print("[Test 2]")
    test_2()

if __name__ == "__main__":
    main()
