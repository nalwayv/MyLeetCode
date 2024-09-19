class Solution:
    def _count_bits(self, val: int) -> int:
        count: int = 0
        while val:
            count += val & 1
            val >>= 1
        return count

    def countBits(self, n: int) -> list[int]:        
        result: list[int] = [0]*(n+1)
        
        for i in range(n+1):
            result[i] = self._count_bits(i)

        return result


def main() -> None:
    print("338. Counting Bits")

    sol = Solution()
    result: list[int] = sol.countBits(5)
    print(result)


if __name__ == "__main__":
    main()