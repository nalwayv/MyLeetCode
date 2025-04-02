class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        """Return the max value over all triplets of indices

        Args:
            nums (list[int])

        Returns:
            int: max value
        """
        n: int = len(nums)
        max_value: int = 0
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    max_value = max(max_value, (nums[i] - nums[j]) * nums[k])

        return max_value
    

def main() -> None:
    print("2873. Maximum Value of an Ordered Triplet I")
    
    sol = Solution()

    print(f"Result= {sol.maximumTripletValue([12,6,1,2,7])}")
    print(f"Result= {sol.maximumTripletValue([1,10,3,4,19])}")
    print(f"Result= {sol.maximumTripletValue([1,2,3])}")


if __name__ == "__main__":
    main()