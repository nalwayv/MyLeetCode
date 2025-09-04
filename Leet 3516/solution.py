class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """
        Determines which of two values (x or y) is closer to a target value z.
        Args:
            x (int): The first value to compare.
            y (int): The second value to compare.
            z (int): The target value.
        Returns:
            int: Returns 1 if x is closer to z, 2 if y is closer to z, or 0 if both are equally close.
        """
        xz: int = abs(x - z)
        yz: int = abs(y - z)

        if xz < yz:
            return 1

        if yz < xz:
            return 2

        return 0


def main() -> None:
    print("3516. Find Closest Person")

    solution = Solution()

    case1: int = solution.findClosest(x=2, y=7, z=4)
    print(f"case 1 should equal 1 ? {case1}")

    case2: int = solution.findClosest(x=2, y=5, z=6)
    print(f"case 2 should equal 2 ? {case2}")

    case3: int = solution.findClosest(x=1, y=5, z=3)
    print(f"case 3 should equal 0 ? {case3}")


if __name__ == "__main__":
    main()
