class Solution:
    def _count_set_bits(self, value: int) -> int:
        """count bits that are set to 1 int value
        """
        # value | bin  | result
        #      -+-    -+-
        #     7 | 0111 | 3
        #    10 | 1010 | 2

        count: int = 0
        while value:
            count += value & 1
            value >>= 1
        return count 

    def minBitFlips(self, start: int, goal: int) -> int:
        return self._count_set_bits(start ^ goal)


def main() -> None:
    print("2220. Minimum Bit Flips to Convert Number")
    
    sol = Solution()
    print(sol.minBitFlips(10, 7))


if __name__ == "__main__":
    main()