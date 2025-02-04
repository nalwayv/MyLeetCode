class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        n: int = len(nums)
        result: int = -1

        for i in range(n):
            for j in range(i+1, n+1):

                sum_total: int = nums[i]
                
                for k in range(i+1, j):
                    if nums[k-1] >= nums[k]:
                        break
                    sum_total += nums[k]

                result = max(result, sum_total)

        return result


def test_case(sol: Solution, nums: list[int], expected: int) -> None:
    result: int = sol.maxAscendingSum(nums)
    test: str = "pass" if result == expected else "fail"
    print(f"Result: {test}")


def main() -> None:
    print("1800. Maximum Ascending Subarray Sum")

    sol = Solution()

    nums_1: list[int] = [10,20,30,5,10,50]
    test_case(sol, nums_1, 65)

    nums_2: list[int] = [10,20,30,40,50]
    test_case(sol, nums_2, 150)

    nums_3: list[int] = [12,17,15,13,10,11,12]
    test_case(sol, nums_3, 33)


if __name__ == "__main__":
    main()