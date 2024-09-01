class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != (n*m):
            return []
        
        result: list[list[int]] = []
        k: int = 0
        for _ in range(m):
            res: list[int] = []
            for _ in range(n):
                res.append(original[k])
                k+=1
            result.append(res)
                
        return result


def test_result(a: list[list[int]], b: list[list[int]]) -> bool:
    row_a: int = len(a)
    row_b: int = len(b)

    if row_a == 0 and row_b == 0:
        return True 

    if row_a != row_b:
        return False

    col_a: int = len(a[0])
    col_b: int = len(b[0])

    if col_a != col_b:
        return False
            
    for i in range(row_a):
        for j in range(col_a):
            if a[i][j] != b[i][j]:
                return False
            
    return True


def case1(sol: Solution) -> None:
    nums: list[int] = [1,2,3,4]
    m: int = 2
    n: int = 2

    result: list[list[int]] = sol.construct2DArray(nums, m, n)
    expect: list[list[int]] = [[1,2],[3,4]]
    
    test: str = "pass" if test_result(result, expect) else "fail"
    print(test)


def case2(sol: Solution) -> None:
    nums: list[int] = [1,2,3]
    m: int = 1
    n: int = 3
    
    result: list[list[int]] = sol.construct2DArray(nums, m, n)
    expect: list[list[int]] = [[1,2,3]]

    test: str = "pass" if test_result(result, expect) else "fail"
    print(test)


def case3(sol: Solution) -> None:
    nums: list[int] = [1,2]
    m: int = 1
    n: int = 1

    result: list[list[int]] = sol.construct2DArray(nums, m, n)
    expect: list[list[int]] = []

    test: str = "pass" if test_result(result, expect) else "fail"
    print(test)


def case4(sol: Solution) -> None:
    nums: list[int] = [1,1,1,1]
    m: int = 4
    n: int = 1

    result: list[list[int]] = sol.construct2DArray(nums, m, n)
    expect: list[list[int]] = [[1],[1],[1],[1]]

    test: str = "pass" if test_result(result, expect) else "fail"
    print(test)


def main() -> None:
    print("2022. Convert 1D Array Into 2D Array")

    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)
    case4(sol)


if __name__ == "__main__":
    main()