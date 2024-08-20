class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n: int = len(gain)
        tmp: list[int] = [0] * (n+1)
        highest: int = 0

        for i in range(n):
            tmp[i+1] = tmp[i] + gain[i]
            highest = max(highest, tmp[i+1])
            
        return highest


def main() -> None:
    print("1732. Find the Highest Altitude")

    sol = Solution()
    print(sol.largestAltitude([-5,1,5,0,-7]) == 1)
    print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0)
    print(sol.largestAltitude([52,-91,72]) == 52)


if __name__ == "__main__":
    main()