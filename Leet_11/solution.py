class Solution:
    def maxArea(self, height: list[int]) -> int:
        n: int = len(height)
        p1: int = 0
        p2: int = n - 1

        area: int = 0

        while p1 < p2:
            a:int = height[p1]
            b:int = height[p2]

            # area is difference between p1 and p2 * min between heights
            new_area: int = (p2 - p1) * min(a, b)

            if new_area >= area:
                area = new_area

            if a < b:
                p1 += 1
            else:
                p2 -= 1

        return area


def main() -> None:
    print("11. Container With Most Water")
    
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
    print(sol.maxArea([1,1]) == 1)


if __name__ == "__main__":
    main()