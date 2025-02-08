class Solution:
    def queryResults(self, queries: list[list[int]]) -> list[int]:
        color: dict[int, int] = {}
        distinct: dict[int, int] = {}
        result: list[int] = []

        for x,y in queries:
            if x in color:
                tmp: int = color[x]
                distinct[tmp] -= 1

                if distinct[tmp] == 0:
                    del distinct[tmp]

            color[x] = y
            distinct[y] = distinct.get(y, 0) + 1


            result.append(len(distinct))

        return result


def main() -> None:
    print("3160. Find the Number of Distinct Colors Among the Balls")

    sol = Solution()

    case_1: list[int] = sol.queryResults([[1,4], [2,5], [1,3], [3,4]])
    print([1,2,2,3], " = ", case_1)

    case_2: list[int] = sol.queryResults([[0,1],[1,2],[2,2],[3,4],[4,5]])
    print([1,2,2,3,4], " = ", case_2)

    case_3: list[int] = sol.queryResults([[0,1],[0,4],[0,4],[0,1],[1,2]])
    print([1,1,1,1,2], " = ", case_3)


if __name__ == "__main__":
    main()