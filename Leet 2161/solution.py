class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lo: list[int] = []
        hi: list[int] = []
        count: int = 0
        for num in nums:
            if num < pivot:
                lo.append(num)
            elif num > pivot:
                hi.append(num)
            else:
                count += 1

        i: int = 0
        for num in lo:
            nums[i] = num
            i += 1
        for _ in range(count):
            nums[i] = pivot
            i += 1
        for num in hi:
            nums[i] = num
            i += 1

        return nums


#-------------------------------------------------------------------
# TEST CASE


def test_case_1(sol: Solution) -> None:
    print("case 1")
    nums: list[int] = [9,12,5,10,14,3,10]
    pivot: int = 10

    result: list[int] = sol.pivotArray(nums, pivot)
    print(result)


def test_case_2(sol: Solution) -> None:
    print("case 2")
    nums: list[int] = [-3,4,3,2]
    pivot: int = 2

    result: list[int] = sol.pivotArray(nums, pivot)
    print(result)


#-------------------------------------------------------------------
# MAIN


def main() -> None:
    print("2161. Partition Array According to Given Pivot")

    sol = Solution()

    test_case_1(sol)
    test_case_2(sol)


if __name__ == "__main__":
    main()