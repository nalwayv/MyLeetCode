class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # NOTE: intervals[i] = [starti, endi]

        # sort by start
        arr: list[list[int]] = sorted(intervals, key=lambda v:v[0])
        result: list[list[int]] = []

        p1: int = 0
        for p2 in range(1, len(arr)):
            # if end >= start
            if arr[p1][1] >= arr[p2][0]:
                # update end to the max of end's
                arr[p1][1] = max(arr[p1][1], arr[p2][1])
            else:
                result.append(arr[p1])
                p1 = p2

        # add what remains
        result.append(arr[p1]) 

        return result


def main() -> None:
    print("56. Merge Intervals")
    sol = Solution()
    result: list[list[int]] = sol.merge([[1,3],[2,6],[8,10],[15,18]])
    # output: [[1,6],[8,10],[15,18]]
    print(result)


if __name__ == "__main__":
    main()