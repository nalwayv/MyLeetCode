class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sorted_nums: list[int] = sorted(nums1 + nums2)
        length: int = len(sorted_nums)

        if length % 2 == 0:
            at: int = length // 2
            return (sorted_nums[at] + sorted_nums[at - 1]) / 2

        return sorted_nums[length // 2]


def main():
    print('4. Median of Two Sorted Arrays')

    solution = Solution()
    case1 = solution.findMedianSortedArrays([1, 3], [2])
    print(case1)
    

if __name__ == '__main__':
    main()