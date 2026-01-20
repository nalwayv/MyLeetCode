class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans: list[int] = []
        for val in nums:
            min_val: int = -1
            for i in range(val):
                if (i | (i+1)) == val:
                    if min_val == -1:
                        min_val = i
                    else:
                        min_val = min(min_val, i)
            ans.append(min_val)
        return ans
    

def main() -> None:
    print('3314. Construct the Minimum Bitwise Array I')

    solution = Solution()
    print(solution.minBitwiseArray([2,3,5,7]))
    print(solution.minBitwiseArray([11,13,31]))


if __name__ == '__main__':
    main()