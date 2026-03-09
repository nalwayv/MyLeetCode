class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        for num in nums:
            k ^= num
        return k.bit_count()


def main() -> None:
    print('2997. Minimum Number of Operations to Make Array XOR Equal to K')

    sol = Solution()
    
    nums = [2,1,3,4]
    result = 'pass' if sol.minOperations(nums, 1) == 2 else 'fail'
    print(f'Case1 should equal 2? {result}')


if __name__ == '__main__':
    main()