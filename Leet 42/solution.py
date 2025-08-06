class Solution:
    def trap(self, height: list[int]) -> int:
        left: int = 0
        right: int = len(height) - 1
        left_max: int = height[left]
        right_max: int = height[right]
        total: int = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                total += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total += max(0, right_max - height[right])

        return total


def main() -> None:
    print("42. Trapping Rain Water")

    sol = Solution()
    
    case_1: int = sol.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1])
    print(f"case 1 should equal 6? {case_1}")
    
    case_2: int = sol.trap(height=[4,2,0,3,2,5])
    print(f"case 2 should equal 9? {case_2}")


if __name__ == "__main__":
    main()
        