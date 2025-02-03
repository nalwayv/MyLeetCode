class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        len_nums: int = len(nums)
        
        max_inc: int = 1
        max_sub: int = 1

        for i in range(len_nums):
            for j in range(i+1, len_nums+1):
                if j - i > 1:
                    sub_nums: list[int] = nums[i : j]
                    len_sub: int = len(sub_nums)

                    inc: int = 1
                    for k in range(1, len_sub):
                        if sub_nums[k-1] >= sub_nums[k]:
                            break
                        inc += 1
                    max_inc = max(max_inc, inc)

                    sub: int = 1
                    for k in range(1, len_sub):
                        if sub_nums[k-1] <= sub_nums[k]:
                            break
                        sub += 1
                    max_sub = max(max_sub, sub)

        return max(max_inc, max_sub)


def test_case(sol: Solution, nums: list[int], expected: int) -> None:
    result: int = sol.longestMonotonicSubarray(nums)
    test: str = "pass" if result == expected else "fail"
    print(f"Result: {test}")


def main() -> None:
    print("3105. Longest Strictly Increasing or Strictly Decreasing Subarray")

    sol = Solution()

    nums_1: list[int] = [1,4,3,3,2]
    test_case(sol, nums_1, 2)

    nums_2: list[int] = [3,3,3,3]
    test_case(sol, nums_2, 1)

    nums_3: list[int] = [3,2,1]
    test_case(sol, nums_3, 3)


if __name__ == "__main__":
    main()