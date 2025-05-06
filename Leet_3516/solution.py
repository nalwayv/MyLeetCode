# Determine which person reaches Person 3 first:

# Return 1 if Person 1 arrives first.
# Return 2 if Person 2 arrives first.
# Return 0 if both arrive at the same time.
# Return the result accordingly.

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz: int = abs(z - x)
        yz: int = abs(z - y)

        if xz < yz:
            return 1
        
        if xz > yz:
            return 2
        
        return 0


def main() -> None:
    print("3516. Find Closest Person")
    
    sol = Solution()
    print(f"Person {sol.findClosest(2,7,4)} is closest to Person 3")


if __name__ == "__main__":
    main()