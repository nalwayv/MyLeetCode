class Solution:
    def _is_even(self, n: int) -> bool:
        return (n ^ 1) == (n + 1)

    def isArraySpecial(self, nums: list[int]) -> bool:
        n: int = len(nums)
        
        if n == 1:
            return True
        
        # An array is special if pairs are not both even or odd
        for i in range(1, n):
            if self._is_even(nums[i-1]) == self._is_even(nums[i]):
                return False
                
        return True


def main() -> None:
    print("3151. Special Array I")

    sol = Solution()

    nums_1: list[int] = [1]
    case_1: bool = sol.isArraySpecial(nums_1)
    print(f"Case 1 {"pass" if case_1 else "fail"}")

    nums_2: list[int] = [2,1,4]
    case_2: bool = sol.isArraySpecial(nums_2)
    print(f"Case 2 {"pass" if case_2 else "fail"}")

    nums_3: list[int] = [4,3,1,6]
    case_3: bool = sol.isArraySpecial(nums_3)
    print(f"Case 3 {"pass" if not case_3 else "fail"}")


if __name__ == "__main__":
    main()