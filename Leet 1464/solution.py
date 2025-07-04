import heapq

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n: int = len(nums)
        if n == 2:
            return (nums[0]-1) * (nums[1]-1)
        
        #Convert heapq to a max heapq
        heap: list[int] = []
        for num in nums:
            heapq.heappush(heap, num * -1)

        a: int = heapq.heappop(heap) * -1
        b: int = heapq.heappop(heap) * -1

        return (a-1) * (b-1)


def main() -> None:
    print("1464. Maximum Product of Two Elements in an Array")

    sol = Solution()
    case1: int = sol.maxProduct([3,4,5,2])
    print(f"Case 1: {"pass" if case1 == 12 else "fail"}")

    case2: int = sol.maxProduct([1,5,4,5])
    print(f"Case 2: {"pass" if case2 == 16 else "fail"}")

    case3: int = sol.maxProduct([3,7])
    print(f"Case 3: {"pass" if case3 == 12 else "fail"}")


if __name__ == "__main__":
    main()