class Solution:
    def _clamp(self, value: int, lo: int, hi: int) -> int:
        return min(hi, max(value, lo))

    # #NOTE: slow with large numbers
    # def divide(self, dividend: int, divisor: int) -> int:
    #     """Divide without using /
    #     """
    #     sign: int = -1 if dividend * divisor < 0 else 1
    #     dividend = abs(dividend)
    #     divisor = abs(divisor)

    #     i: int = 0
    #     while dividend >= divisor:
    #         dividend -= divisor
    #         i += 1

    #     return sign * i

    def divide(self, dividend: int, divisor: int) -> int:
        sign: int = -1 if dividend * divisor < 0 else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        mask: int = 1
        i: int = 0

        while divisor <= dividend:
            divisor <<= 1
            mask <<= 1

        while mask > 1:
            divisor >>= 1
            mask >>= 1

            if dividend >= divisor:
                dividend -= divisor
                i |= mask

        return self._clamp(sign * i, -2147483648, 2147483647)


def main() -> None:
    print("29. Divide Two Integers")
    
    sol = Solution()
    print(sol.divide(10, 2))
    print(sol.divide(2147483647, 3))


if __name__ == "__main__":
    main()