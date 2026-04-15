class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        min_dist: float = float('inf')
        n: int = len(words)
        inc: int = -1
        dec: int = -1

        for i in range(n):
            inc += 1
            dec += 1

            if words[(startIndex + i) % n] == target:
                min_dist = min(min_dist, inc)

            if words[(startIndex - i) % n] == target:
                min_dist = min(min_dist, dec)
        
        return -1 if min_dist == float('inf') else int(min_dist)


def main() -> None:
    print('2515. Shortest Distance to Target String in a Circular Array')

    sol = Solution()
    case1: int = sol.closestTarget(words = ['hello','i','am','leetcode','hello'], target = 'hello', startIndex = 1)
    print(f'Result: {case1}')
    
    case2: int = sol.closestTarget(words = ['a','b','leetcode'], target = 'leetcode', startIndex = 0)
    print(f'Result: {case2}')
    
    case3: int = sol.closestTarget(words = ['i','eat','leetcode'], target = 'ate', startIndex = 0)
    print(f'Result: {case3}')


if __name__ == '__main__':
    main()