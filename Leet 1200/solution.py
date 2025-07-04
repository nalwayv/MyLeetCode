class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """
        Given an array of distinct integers arr
        find all pairs of elements with the minimum absolute difference of any two elements.
        """
        n: int = len(arr)
        sorted_arr: list[int] = sorted(arr)

        diff: float = float("inf")
        result: list[list[int]] = []
        
        for i in range(1, n):
            # get absolute difference between sorted values
            new_diff: float = float(sorted_arr[i] - sorted_arr[i - 1])

            # start again with new diff or continue with original
            if new_diff < diff:
                diff = new_diff
                result.clear()
                result.append([sorted_arr[i - 1], sorted_arr[i]])

            elif new_diff == diff:
                result.append([sorted_arr[i - 1], sorted_arr[i]])

        return result


def case1(sol: Solution) -> None:
    arr: list[int] = [4, 2, 1, 3]
    result: list[list[int]] = sol.minimumAbsDifference(arr)
    print(f"Case 1: {result} == [[1, 2], [2, 3], [3, 4]]")


def case2(sol: Solution) -> None:
    arr: list[int] = [1, 3, 6, 10, 15]
    result: list[list[int]] = sol.minimumAbsDifference(arr)
    print(f"Case 2: {result} == [[1, 3]]")


def case3(sol: Solution) -> None:
    arr: list[int] = [3, 8, -10, 23, 19, -4, -14, 27]
    result: list[list[int]] = sol.minimumAbsDifference(arr)
    print(f"Case 3: {result} == [[-14, -10], [19, 23], [23, 27]]")


def main() -> None:
    print("1200. Minimum Absolute Difference")

    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()