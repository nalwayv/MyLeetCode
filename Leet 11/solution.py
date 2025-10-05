class Solution:
    def maxArea(self, height: list[int]) -> int:
        length: int = len(height)
        left: int = 0
        right: int = length - 1
        max_area: int = 0

        while left < right:
            # area = width * height
            width: int = right - left
            max_area = max(max_area, width * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def main() -> None:
    print("11. Container With Most Water")
    
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
    print(sol.maxArea([1,1]) == 1)


if __name__ == "__main__":
    main()