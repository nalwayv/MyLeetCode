class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        def grid_row_or_col_string_builder(grid: list[list[int]], n: int, i: int, row:bool = False) -> str:
            """helper to build a string from grid row or col values
            """
            str_builder: list[str] = ["["]

            for j in range(n):
                if row:
                    if j+1 >= n:
                        str_builder.append(str(grid[i][j]))
                    else:
                        str_builder.append(f"{str(grid[i][j])},")
                else:
                    if j+1 >= n:
                        str_builder.append(str(grid[j][i]))
                    else:
                        str_builder.append(f"{str(grid[j][i])},")

            str_builder.append("]")
            return "".join(str_builder)
        

        def get_dict_of_column_patterns(grid: list[list[int]]) -> dict[str, int]:
            """return dict of each column pattern and the amount of times it appears
            """
            result: dict[str, int] = {}

            n: int = len(grid[0])
            for i in range(n):
                # add how many times column pattern appears in grid
                str_num: str = grid_row_or_col_string_builder(grid, n, i)
                if str_num not in result:
                    result[str_num] = 1
                else:
                    result[str_num] += 1

            return result
        

        n: int = len(grid)
        cols: dict[str, int] = get_dict_of_column_patterns(grid)
        count: int = 0
        
        for i in range(n):
            str_num: str = grid_row_or_col_string_builder(grid, n, i, True)

            # add how many times row's pattern appears within columns
            if str_num in cols:
                count += cols[str_num]
        
        return count


def case_1(sol: Solution) -> None:
    grid = [
        [3,2,1],
        [1,7,6],
        [2,7,7]
    ]
    print(sol.equalPairs(grid) == 1)


def case_2(sol: Solution) -> None:
    grid = [
        [3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]]
    
    # 3
    # row 0 col 0 = 3122
    # row 2 col 2 = 2422
    # row 3 col 2 = 2422

    print(sol.equalPairs(grid) == 3)


def case_3(sol: Solution) -> None:
    grid = [
        [3,1,2,2],
        [1,4,4,4],
        [2,4,2,2],
        [2,5,2,2]]
    print(sol.equalPairs(grid) == 3)


def case_4(sol: Solution) -> None:
    grid = [
        [11,1],
        [1,11]]
    print(sol.equalPairs(grid) == 2)


def case_5(sol: Solution) -> None:
    grid = [[1]]
    print(sol.equalPairs(grid) == 1)


def main() -> None:
    print("2352. Equal Row and Column Pairs")

    sol = Solution()
    
    case_1(sol)
    case_2(sol)
    case_3(sol)
    case_4(sol)
    case_5(sol)


if __name__ == "__main__":
    main()