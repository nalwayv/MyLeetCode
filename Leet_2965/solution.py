class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        result: list[int] = []
        seen: set[int] = set()
        count: int = 0

        for row in grid:
            for num in row:
                count += 1
                if num not in seen:
                    seen.add(num)
                else:
                    result.append(num)

        for i in range(1, count+1):
            if i not in seen:
                result.append(i)

        return result


#------------------------------------------------------------------------------
# TEST CASE


def test_case_1(sol: Solution) -> None:
    grid: list[list[int]] = [[1,3], [2,2]]
    result: list[int] = sol.findMissingAndRepeatedValues(grid)
    print(f"Case1: {result}")


def test_case_2(sol: Solution) -> None:
    grid: list[list[int]] = [[9,1,7],[8,9,2],[3,4,6]]
    result: list[int] = sol.findMissingAndRepeatedValues(grid)
    print(f"Case2: {result}")


#------------------------------------------------------------------------------
# MAIN


def main() -> None:
    print("2965. Find Missing and Repeated Values")

    solution = Solution()
    test_case_1(solution)
    test_case_2(solution)


if __name__ == "__main__":
    main()