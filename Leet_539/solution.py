from datetime import datetime, timedelta

class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        n: int = len(timePoints)
        format: str = "%H:%M"
        datetimes: list[datetime] = [datetime.strptime(tp, format) for tp in timePoints]

        datetimes.sort()

        diff: int = (datetimes[0] - datetimes[-1]).seconds // 60
        for i in range(n-1):
            difference: timedelta = datetimes[i+1] - datetimes[i]
            diff = min(diff, difference.seconds // 60)

        return diff


def main() -> None:    
    print("539. Minimum Time Difference")

    sol = Solution()

    print(sol.findMinDifference(["23:59","00:00"]))
    print(sol.findMinDifference(["00:00","23:59","00:00"]))
    print(sol.findMinDifference(["01:30","01:35", "01:50"]))


if __name__ == "__main__":
    main()