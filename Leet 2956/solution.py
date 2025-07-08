class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a: int = 0
        for val in nums1:
            if val in nums2:
                a += 1
        
        b: int = 0
        for val in nums2:
            if val in nums1:
                b += 1

        return [a, b]


def main() -> None:
    print("2956. Find Common Elements Between Two Arrays")
    sol = Solution()

    print("case 1")
    print(sol.findIntersectionValues([2,3,2], [1,2]))
    
    print("case 2")
    print(sol.findIntersectionValues([4,3,2,3,1],[2,2,5,2,3,6]))

    print("case 3")
    print(sol.findIntersectionValues([3,4,2,3], [1,5]))


if __name__ == "__main__":
    main()