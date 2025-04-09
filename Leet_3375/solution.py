class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        values: set[int] = set()
        
        for num in nums:
            if num < k:
                return -1
            
            if num > k:
                values.add(num)

        return len(values)


def main() -> None:
    print("3375. Minimum Operations to Make Array Values Equal to K")
    
    sol = Solution()

    nums: list[int] = [5,2,5,4,5]
    k: int = 2
    expect: int = 2
    result: int = sol.minOperations(nums, k)
    print(f"Case 1: {"pass" if result == expect else "fail"}")


if __name__ == "__main__":
    main()