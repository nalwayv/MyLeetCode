class Solution:
    def _findMaxAverage(self, nums: list[int], k: int) -> float:
        n: int = len(nums)
        max_avg: float = -1.0

        for i in range(0, n - k + 1):
            add: int = 0
            for j in range(k):
                add += nums[i+j]

            avg: float = float(add / k)

            if avg > max_avg:
                max_avg = avg

        return max_avg

    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n:int = len(nums)

        max_sum: float = float(sum(nums[:k]))
        max_avg: float = max_sum / k
        current: float = max_sum

        for i in range(k, n):
            current += float(nums[i] - nums[i-k])
            avg: float = current / k
            if avg > max_avg:
                max_avg = avg

        return max_avg
    

def main() -> None:
    print("643. Maximum Average Subarray I")
    sol = Solution()
    nums: list[int] = [1,12,-5,-6,50,3]
    k: int = 4
    result: float = sol.findMaxAverage(nums, k)
    print(f"Avg: {result}")


if __name__ == "__main__":
    main()