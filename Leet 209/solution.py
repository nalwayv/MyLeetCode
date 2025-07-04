class Solution:
    """
    Given an array of positive integers nums and a positive integer target, 

    return the minimal length of a subarray whose sum is greater than or equal to target. 

    If there is no such subarray, return 0 instead.

    Example:
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    """
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n: int = len(nums)
        total: int = nums[0]
        result: int = 0
        p1: int = 0
        p2: int = 1

        while p2 <= n:
            if total >= target:
                result = min(result, p2 - p1) if result != 0 else p2 - p1
                total -= nums[p1]
                p1 += 1
            else:
                # clamp to prevent out of bounds
                total += nums[max(0, min(p2, n-1))]
                p2 += 1

        return result
    
    def minSubArrayLen2(self, target: int, nums: list[int]) -> int:
        p1: int = 0
        p2: int = 0
        n: int = len(nums)
        result: int = 0

        while p2 < n:
            sum_: int = 0
            while p2 < n and not (sum_ >= target):
                sum_ += nums[p2]
                p2 += 1

            if sum_ >= target:
                if result == 0:
                    result = p2 - p1
                else:
                    result = min(result, p2 - p1)

                p1 += 1
                p2 = p1

        return result
    

def main() -> None:
    solution = Solution()
    print(f"Output: {solution.minSubArrayLen(7, [2,3,1,2,4,3])}")# = 2
    print(f"Output: {solution.minSubArrayLen(4, [1,4,4])}")# = 1
    print(f"Output: {solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1])}")# = 0
    print(f"Output: {solution.minSubArrayLen(11, [1,2,3,4,5])}")# = 3
    print(f"Output: {solution.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8])}")# = 2
    print(f"Output: {solution.minSubArrayLen(7, [2,3,1,2,4,3])}")# = 2

    # print(f"Output: {solution.minSubArrayLen2(7, [2,3,1,2,4,3])}")# = 2
    # print(f"Output: {solution.minSubArrayLen2(4, [1,4,4])}")# = 1
    # print(f"Output: {solution.minSubArrayLen2(11, [1,1,1,1,1,1,1,1])}")# = 0
    # print(f"Output: {solution.minSubArrayLen2(11, [1,2,3,4,5])}")# = 3
    # print(f"Output: {solution.minSubArrayLen2(15, [5,1,3,5,10,7,4,9,2,8])}")# = 2

if __name__ == "__main__":
    main()
    