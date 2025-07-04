class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        n: int = len(nums)

        # create frequency table and also record max frequency value
        table: dict[int, int] = {}
        max_frequency: int = 0

        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
            max_frequency = max(max_frequency, table[num])

        # get smallest range
        result: int = n
        for key, val in table.items():
            if val == max_frequency:
                lo: int = 0
                hi: int = n

                while lo < hi - 1 and nums[lo] != key:
                    lo += 1

                while hi > 0 and nums[hi-1] != key:
                    hi -= 1

                result = min(result, hi - lo)

        return result


# ** Test Cases **


def test_case(sol: Solution, nums: list[int], expected: int) -> None:
    result: int = sol.findShortestSubArray(nums)
    result_str: str = "pass" if result == expected else "fail"
    print(f"Case findShortestSubArray({nums}) == {expected}: {result_str}")


# ** Main **


def main() -> None:
    print("697. Degree of an Array")

    sol = Solution()

    test_case(sol, [1,2,2,3,1], 2)
    test_case(sol, [1,2,2,3,1,4,2], 6)
    test_case(sol, [1,5,2,3,5,4,5,6], 6)
    test_case(sol, [2,2,1,1,1,2], 3)
    test_case(sol, [1], 1)
    test_case(sol, [2,1], 1)


if __name__ == "__main__":
    main()