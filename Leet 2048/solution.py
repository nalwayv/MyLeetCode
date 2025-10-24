from collections import Counter

class Solution:
    def is_beautiful(self, num: int) -> bool:
        count = Counter(x for x in str(num))
        return all(int(k) == v for k,v in count.items())

    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while not self.is_beautiful(n):
            n += 1
        return n


def test_case(sol: Solution, n: int, expected: int) -> None:
    result: int = sol.nextBeautifulNumber(n)
    test: str = 'pass' if result == expected else 'fail'
    print(f'{n} should equal {expected}?: {test}')


def main() -> None:
    print('2048. Next Greater Numerically Balanced Number')

    sol = Solution()
    
    test_case(sol, 1, 22)
    test_case(sol, 1000, 1333)
    test_case(sol, 3000, 3133)


if __name__ == "__main__":
    main()