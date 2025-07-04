class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for fac in [5, 3, 2]:
            while n % fac == 0:
                n //= fac

        return n == 1


def main() -> None:
    print("263. Ugly Number")
    
    sol = Solution()

    print(f"Case 1: 6 is {"ugly" if sol.isUgly(6) else "not uglt"}")
    print(f"Case 2: 1 is {"ugly" if sol.isUgly(1) else "not uglt"}")
    print(f"Case 3: 114 is {"ugly" if sol.isUgly(14) else "not uglt"}")


if __name__ == "__main__":
    main()