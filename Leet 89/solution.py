class Solution:
    def grayCode(self, n: int) -> list[int]:
        return [i ^ (i >> 1) for i in range(2 ** n)]


def main() -> None:
    print('89. Gray Code')
    
    solution = Solution()

    gray_numbers = solution.grayCode(2)
    print('n == 2')
    for num in gray_numbers:
        print(num)


if __name__ == '__main__':
    main()