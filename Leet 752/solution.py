from collections import deque

class Solution:
    """
    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
    """ 
    def pack(self, n0: int, n1: int, n2: int, n3: int) -> int:
        return n3 << 16 | n2 << 12 | n1 << 8 | n0 << 4
    
    def openLock(self, deadends: list[str], target: str) -> int:
        # using bit-packing to avoid using strings
        # max pack 9999 using 4->16 bit == 629136

        # v: list[bool] = [False] * 9999
        # for d in deadends:
        #     p: int =self.pack(int(d[0]), int(d[1]), int(d[2]), int(d[3]))
        #     v[p % 9999]=True
        visited: set[int] = set() # len 0-9999
        for d in deadends:
            visited.add(self.pack(int(d[0]), int(d[1]), int(d[2]), int(d[3])))

        target_p: int = self.pack(int(target[0]), int(target[1]), int(target[2]), int(target[3]))

        code: list[int] = [0,0,0,0]
        n1: list[int] = [0,0,0,0]
        n2: list[int] = [0,0,0,0]
        
        step: int = 0
        que: deque[int] = deque()
        que.appendleft(0)
        while que:

            size: int = len(que)

            for _ in range(size):
                current: int = que.popleft()

                if current in visited:
                    continue
                
                # if v[current % 9999]:
                #     continue

                if current == target_p:
                    return step
                    
                visited.add(current)
                # v[current % 9999] = True
                
                # unpack
                code[0] = (current >> 4) & 0xF
                code[1] = (current >> 8) & 0xF
                code[2] = (current >> 12) & 0xF
                code[3] = (current >> 16) & 0xF

                for i in range(4):
                    for j in range(4):
                        if i == j:
                            # wrap
                            n1[j] = (code[j] + 9) % 10
                            n2[j] = (code[j] + 1) % 10
                        else:
                            n1[j] = code[j]
                            n2[j] = code[j]
                    
                    p1: int = self.pack(n1[0], n1[1], n1[2], n1[3])
                    que.append(p1)
                        
                    p2: int = self.pack(n2[0], n2[1], n2[2], n2[3])
                    que.append(p2)
                
                print(f"que size = {len(que)}")

            step += 1
        return -1


def test1(solution: Solution) -> None:
    print("Test1:", end=" ")
    deadends: list[str] = ["0201","0101","0102","1212","2002"]
    target: str = "0202"
    result: int = solution.openLock(deadends, target)
    print(f"Expected 6, Output {result}")


def test2(solution: Solution) -> None:
    print("Test2:", end=" ")
    deadends: list[str] = ["8888"]
    target: str = "0009"
    result: int = solution.openLock(deadends, target)
    print(f"Expected 1, Output {result}")


def test3(solution: Solution) -> None:
    print("Test3:", end=" ")
    deadends: list[str] = ["8887","8889","8878","8898","8788","8988","7888","9888", "7888"]
    target: str = "8888"
    result: int = solution.openLock(deadends, target)
    print(f"Expected -1, Output {result}")


def main() -> None:
    solution = Solution()
    test1(solution)
    test2(solution)
    test3(solution)


if __name__ == "__main__":
    main()