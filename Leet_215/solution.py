import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap: list[int] = []
        for num in nums:
            heapq.heappush(heap, num * -1)

        result: int = -1
        for _ in range(k):
            result = heapq.heappop(heap)
        return result * -1
        

def main() -> None:
    print("215. Kth Largest Element in an Array")

    sol = Solution()
    nums: list[int] = [3,2,1,5,6,4]
    k: int = 2
    result: int = sol.findKthLargest(nums, k)
    print(f"case 1 {"pass" if result == 5 else "fail"}")


if __name__ == "__main__":
    main()