class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        m: int = 1000000007

        for q in queries:
            l,r,k,v = q

            if r > len(nums):
                continue
            
            idx: int = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % m
                idx += k

        result: int = nums[0]
        for num in nums[1:]:
            result ^= num
            
        return result


def main() -> None:
    print('3653. XOR After Range Multiplication Queries I')
    solution = Solution()
    result: int = solution.xorAfterQueries([1,1,1], [[0,2,1,4]])
    print(result)


if __name__ == '__main__':
    main()