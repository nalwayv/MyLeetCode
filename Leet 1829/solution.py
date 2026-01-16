class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] ^= nums[i-1]
        
        max_val: int = (1 << maximumBit) - 1
        result: list[int] = []
        for i in range(len(nums) -1, -1, -1):
            result.append(nums[i] ^ max_val)

        return result


def main() -> None:
    print('1829. Maximum XOR for Each Query')

    solution = Solution()
    
    print(solution.getMaximumXor([0,1,1,3], 2))
    print(solution.getMaximumXor([2,3,4,7], 3))
    print(solution.getMaximumXor([0,1,2,2,5,7], 3))


if __name__ == '__main__':
    main()
