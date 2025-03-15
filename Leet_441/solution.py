class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Return number of compleated stairs where aranging `n` coins could build a staircase
        """
        # n = 5
        #
        # 1 2
        #
        #   * *
        # * * *
        #------

        # n = 8
        #
        # 1 2 3
        #
        #     *
        #   * * *
        # * * * *
        # -------

        i: int = 1
        j: int = 2
        count: int = 0

        while n > 0:
            n -= j
            count = i
            
            i += 1
            j += 1

        return count


# ----------
# TEST


def test_case(sol: Solution, n: int, expected: int) -> None:
    print(f"Case arrangeCoins({n}) == {expected}")
    print(f"{"":>2}{"pass" if sol.arrangeCoins(n) == expected else "fail"}")


# ----------
# MAIN


def main() -> None:
    print("441. Arranging Coins")

    sol = Solution()

    test_case(sol, 5, 2)
    test_case(sol, 8, 3)


if __name__ == "__main__":
    main()