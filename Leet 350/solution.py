class Solution:
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    
    Each element in the result must appear as many times as it shows in both arrays 
    
    and you may return the result in any order.
    """
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # build table of numbers and the times they appear
        table: dict[int, int] = {}
        for val in nums1:
            if val in table:
                table[val] += 1
            else:
                table[val] = 1

        result: list[int] = []
        for val in nums2:
            # only add if in table and amount left is > 0
            if val in table and table[val] > 0:
                result.append(val)
                table[val] -= 1

        return result
    

def main() -> None:
    solution = Solution()
    print(f"Output: {solution.intersect([1,2,2,1], [2,2])}")
    print(f"Output: {solution.intersect([4,9,5], [9,4,9,8,4])}")


if __name__ == "__main__":
    main()