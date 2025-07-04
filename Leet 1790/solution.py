
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n: int = len(s1)
        m: int = len(s2)
        if n != m:
            return False
        
        letters2: list[str] = [ch for ch in s2]
        
        for i in range(n):
            for j in range(i+1, n):

                if s1[i] == s2[j] and s1[j] == s2[i]:
                    # swap
                    letters2[i], letters2[j] = letters2[j], letters2[i]
                    # check
                    if "".join(letters2) == s1:
                        return True
                    # unswap
                    letters2[i], letters2[j] = letters2[j], letters2[i]

        return False


def test_case(sol: Solution, s1: str, s2: str, expect: bool) -> None:
    test: bool = sol.areAlmostEqual(s1, s2)
    result: str = "pass" if test == expect else "fail"
    print(f"Case: {result}")


def main() -> None:
    print("1790. Check if One String Swap Can Make Strings Equal")

    sol = Solution()
    
    test_case(sol, "bank", "kanb", True)
    test_case(sol, "attack", "defend", False)
    test_case(sol, "kelb", "kelb", True)


if __name__ == "__main__":
    main()
