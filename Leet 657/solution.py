class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x: int = 0
        y: int = 0
        for move in moves:
            if move == 'U':
                y += 1
            if move == 'D':
                y -= 1
            if move == 'L':
                x -= 1
            if move == 'R':
                x += 1
        return x == 0 and y == 0


def main() -> None:
    print('657. Robot Return to Origin')
    solution = Solution()

    case1: bool = solution.judgeCircle('UD')
    case1_result = 'pass' if case1 == True else 'fail'
    print(f'case 1 should equal true? {case1_result}')

    case2: bool = solution.judgeCircle('LL')
    case2_result = 'pass' if case2 != True else 'fail'
    print(f'case 1 should equal false? {case2_result}')


if __name__ == '__main__':
    main()