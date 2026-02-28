class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binaries: list[str] = []

        for i in range(1, n + 1):
            binaries.append(bin(i)[2:])

        return int(''.join(binaries), 2) % (10**9 + 7)


def main() -> None:
    print('1680. Concatenation of Consecutive Binary Numbers')
    
    solution = Solution()

    print(solution.concatenatedBinary(1))
    print(solution.concatenatedBinary(3))
    print(solution.concatenatedBinary(12))


if __name__ == '__main__':
    main()