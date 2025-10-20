from collections import Counter

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        counter = Counter(operations)

        neg: int = counter['--X'] + counter['X--']
        pos: int = counter['++X'] + counter['X++']

        return pos - neg
        

def test_case(sol: Solution, operations: list[str], expected: int) -> None:
    result: int = sol.finalValueAfterOperations(operations)
    test: str = 'pass' if result == expected else 'fail'
    print(f'should equal {expected}?', end='')
    print(f'{'':>2} {test}')


def main() -> None:
    print('2011. Final Value of Variable After Performing Operations')

    sol = Solution()
    test_case(sol, ['--X','X++','X++'], 1)
    test_case(sol, ['++X','++X','X++'], 3 )
    test_case(sol, ['X++','++X','--X','X--'], 0)


if __name__ == '__main__':
    main()