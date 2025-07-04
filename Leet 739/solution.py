class Stack:
    def __init__(self) -> None:
        self.values: list[int] = []

    def empty(self) -> bool:
        return len(self.values) == 0

    def push(self, value: int) -> None:
        self.values.append(value)

    def pop(self) -> bool:
        if not self.values:
            return False
        self.values.pop()
        return True
    
    def top(self) -> int:
        return self.values[-1]
    
    def to_str(self) -> str:
        return ", ".join(reversed([str(i) for i in self.values]))


class StackNode:
    def __init__(self) -> None:
        self.value: int = 0
        self.next:StackNode|None = None

class StackL:
    def __init__(self) -> None:
        self.root: StackNode|None = None

    def empty(self) -> bool:
        return self.root == None
    
    def push(self, value: int) -> None:
        node: StackNode = StackNode()

        node.value = value
        node.next = self.root
        self.root = node

    def pop(self) -> bool:
        if not self.root:
            return False        

        self.root = self.root.next
        return True
    
    def top(self) -> int:
        assert self.root != None

        return self.root.value
        
    def to_str(self) -> str:
        assert self.root != None
        result: str = ""
        curr = self.root

        while curr != None:
            result += f"{curr.value}, "
            curr = curr.next

        return result
    
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n: int = len(temperatures)
        answer: list[int] = [0] * n
        stk: Stack = Stack()

        for i in range(n):
            while not stk.empty():
                start: int = stk.top()
                end: int = i

                if temperatures[start] > temperatures[end]:
                    break
                
                # start start to the diff in indexes between end and start
                answer[start] = end - start
                stk.pop()

            stk.push(i)

        return answer


def main() -> None:
    solution = Solution()
    #                0  1  2  3  4  5  6  7
    temperatures = [73,74,75,71,69,72,76,73]
    #              [ 1, 1, 4, 2, 1, 1, 0, 0]
    result = solution.dailyTemperatures(temperatures)
    print(result)

if __name__ == "__main__":
    main()
