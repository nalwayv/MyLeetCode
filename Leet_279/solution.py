from collections import deque

class Solution:
    """
    Given an integer n, return the least number of perfect square numbers that sum to n.

    A perfect square is an integer that is the square of an integer; in other words, 
    
    it is the product of some integer with itself.
     
    For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
    """
    def is_perfect(self, num: int) -> bool:
        """
        check if a number is a perfect square
        """
        lo: int = 1
        hi: int = num

        while lo <= hi:
            m: int = (lo + hi) // 2
            sq: int = m * m
            
            if sq == num:
                return True
            
            if sq < num:
                lo = m + 1
            else:
                hi = m - 1
            
        return False
    
    def numSquares(self, n: int) -> int:
        if self.is_perfect(n):
            return 1
        
        # pre calc prefect squares
        psq: list[int] = [i for i in range(n) if self.is_perfect(i)]

        que: deque[int] = deque()
        que.append(n)

        visited: set[int] = set()

        step: int = 0
        while que:
            size: int = len(que)
            for _ in range(size):
                current: int = que.popleft()

                if current == 0:
                    return step
                
                if current in visited or current < 0:
                    continue

                visited.add(current)

                for p in psq:
                    que.append(current - p)

            step += 1

        return -1
    

def test1(s: Solution) -> None:
    print("test 1 ")
    result: int = s.numSquares(12)
    print(f"Output: {result} Expected: 3")


def test2(s: Solution) -> None:
    print("test 2 ")
    result: int = s.numSquares(13)
    print(f"Output: {result} Expected: 2")


def test3(s: Solution) -> None:
    print("test 3 ")
    result: int = s.numSquares(20)
    print(f"Output: {result} Expected: 2")


def test4(s: Solution) -> None:
    print("test 4 ")
    result: int = s.numSquares(4)
    print(f"Output: {result} Expected: 1")


def main() -> None:
    solution = Solution()
    test1(solution)
    test2(solution)
    test3(solution)
    test4(solution)


if __name__ == "__main__":
    main()