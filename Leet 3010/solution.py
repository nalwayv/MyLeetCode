class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        snums = sorted(nums[1:])
        a: int = nums[0]
        b: int = snums[0]
        c: int = snums[1]
        return a + b + c


def main() -> None:
    print('3010. Divide an Array Into Subarrays With Minimum Cost I')
    solution = Solution()
    print(solution.minimumCost([1,2,3,12]))


if __name__ == '__main__':
    main()
