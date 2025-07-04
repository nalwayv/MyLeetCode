class DContainer:
    def __init__(self, value: int) -> None:
        self.value: int = value


class DNode:
    def __init__(self) -> None:
        self.container: DContainer|None = None
        self.next: DNode|None = None
        self.prev: DNode|None = None


class MyCircularDeque:
    def __init__(self, k: int) -> None:
        self._head: DNode|None = DNode() # dummy
        self._head.next = self._head
        self._head.prev = self._head

        self._length: int = 0
        self._amount: int = k

    def _new_link(self, prev: DNode|None, next: DNode|None, val: int) -> DNode|None:
        if not prev or not next:
            return None
        
        link = DNode()
        link.container = DContainer(val)
        link.prev = prev
        link.next = next

        return link

    def _front(self, node: DNode|None) -> DNode|None:
        return node.next if node else None

    def _last(self, node: DNode|None) -> DNode|None:
        return node.prev if node else None

    def _connect_neighbours(self, node: DNode|None) -> None:
        if not node:
            return
        
        if node.next:
            node.next.prev = node
        
        if node.prev:
            node.prev.next = node

    def _unlink(self, node: DNode|None) -> None:
        if not node:
            return
        
        if node.next:
            node.next.prev = node.prev
    
        if node.prev:
            node.prev.next = node.next
    
    def _instert_after(self, node: DNode|None, value: int) -> None:
        if not node:
            return
        
        self._connect_neighbours(self._new_link(node, node.next, value))

    def _insert_before(self, node: DNode|None, value: int) -> None:
        if not node:
            return
        
        self._instert_after(node.prev, value)

    def _delete_link(self, node: DNode|None):
        self._unlink(node)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self._instert_after(self._head, value)
        self._length += 1
        
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self._insert_before(self._head, value)
        self._length += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self._unlink(self._front(self._head))
        self._length -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self._unlink(self._last(self._head))
        self._length -= 1

        return True

    def getFront(self) -> int:
        node: DNode|None = self._front(self._head)
        if node == None or node.container == None:
            return -1
        
        return node.container.value

    def getRear(self) -> int:
        node: DNode|None = self._last(self._head)
        if node == None or node.container == None:
            return -1
        
        return node.container.value

    def isEmpty(self) -> bool:
        return self._length == 0

    def isFull(self) -> bool:
        return self._length == self._amount


def main() -> None: 
    print("641. Design Circular Deque")

    c_que = MyCircularDeque(3)

    print(f"insert last { "pass" if c_que.insertLast(1) else "fail" }")
    print(f"insert last { "pass" if c_que.insertLast(2) else "fail" }")
    print(f"insert front { "pass" if c_que.insertFront(3) else "fail" }")
    print(f"insert front { "pass" if not c_que.insertFront(4) else "fail" }")
    print(f"get rear { "pass" if c_que.getRear() == 2 else "fail" }")
    print(f"is full { "pass" if c_que.isFull() else "fail" }")
    print(f"delete last { "pass" if c_que.deleteLast() else "fail" }")
    print(f"insert front { "pass" if c_que.insertFront(4) else "fail" }")
    print(f"get front { "pass" if c_que.getFront() == 4 else "fail" }")


if __name__ == "__main__":
    main()