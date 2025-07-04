class Solution:
    """
    Given an integer array nums and an integer k, 
    
    return true if there are two distinct indices i and j in the array 
    
    such that nums[i] == nums[j] and abs(i - j) <= k.
    """
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        ## bad way
        n: int = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j] and abs(i-j)<=k:
                    return True
        return False


    def containsNearbyDuplicate2(self, nums: list[int], k: int) -> bool:
        table: dict[int, int] = {}
        # i != j
        # nums[i] == nums[j]
        # abs(i-j) <= k

        for i, val in enumerate(nums):
            if val not in table:
                table[val] = i
            else:
                # check condition else update table to have current index
                # so as to not keep checking agains the same index
                j: int = table[val]
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
                
                table[val] = i

        return False


def main() -> None:
    solution = Solution()
    print(f"Output: {solution.containsNearbyDuplicate2([1,2,3,1], 3)}") # True
    print(f"Output: {solution.containsNearbyDuplicate2([1,0,1,1], 1)}") # True
    print(f"Output: {solution.containsNearbyDuplicate2([1,2,3,1,2,3], 2)}") # False


if __name__ == "__main__":
    main()