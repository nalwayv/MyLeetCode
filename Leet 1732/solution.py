class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        total_tum = 0
        max_height = 0
        for g in gain:
            total_tum += g
            max_height = max(max_height, total_tum)
        return max_height


def main() -> None:
    print("1732. Find the Highest Altitude")

    sol = Solution()
    print(sol.largestAltitude([-5,1,5,0,-7]) == 1)
    print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0)
    print(sol.largestAltitude([52,-91,72]) == 52)


if __name__ == "__main__":
    main()