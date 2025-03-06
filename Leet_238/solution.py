class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n: int = len(nums)

        prefix: list[int] = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix: list[int] = [1] * n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            nums[i] = prefix[i] * suffix[i]

        return nums


#--------------------------------------------------------------------------
# TEST CASES


def case1(sol: Solution) -> None:
    nums: list[int] = [1,2,3,4]
    result: list[int] = sol.productExceptSelf(nums)
    print(f"Case1: {result} == [24,12,8,6]")


def case2(sol: Solution) -> None:
    nums: list[int] = [-1,1,0,-3,3]
    result: list[int] = sol.productExceptSelf(nums)
    print(f"Case1: {result} == [0,0,9,0,0]")


#--------------------------------------------------------------------------
# MAIN


def main() -> None:
    print("238. Product of Array Except Self")
    sol = Solution()
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()