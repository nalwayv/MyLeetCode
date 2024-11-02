class Solution:
    def _slope(self, p1: list[int], p2: list[int]) -> float:
        """Return the slope of a line bwteen two points
        """
        y:float = float(p2[1] - p1[1])
        x:float = float(p2[0] - p1[0])
        return 0 if x == 0 else y / x

    def _triangle_area(self, p1: list[int], p2: list[int], p3: list[int]) -> float:
        """Return the area of a triangle
        """
        area: int = p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])
        return area * 0.5

    def minimumLines(self, stockPrices: list[list[int]]) -> int:
        n: int = len(stockPrices)

        if n <= 1:
            return 0
        
        if n == 2:
            return 1

        sortedPrices:list[list[int]] = sorted(stockPrices, key=lambda k: [k[0], k[1]])

        slope: float = self._slope(sortedPrices[0], sortedPrices[1])

        # line used for tri area
        l1: list[int] = sortedPrices[0]
        l2: list[int] = sortedPrices[1]

        count:int = 1
        
        for i in range(2, n):
            new_slope: float = self._slope(sortedPrices[i-1], sortedPrices[i])
            
            # check slope and area for small float differeces
            if new_slope != slope or self._triangle_area(l1, l2, sortedPrices[i]) != 0:
                count += 1
                
                slope = new_slope

                l1 = sortedPrices[i-1]
                l2 = sortedPrices[i]

        return count


def case1(solution: Solution) -> None:
    stockPrices: list[list[int]] = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
    result: int = solution.minimumLines(stockPrices)
    print(f"case 1 {result} == 3")


def case2(solution: Solution) -> None:
    stockPrices: list[list[int]] = [[3,4],[1,2],[7,8],[2,3]]
    result: int = solution.minimumLines(stockPrices)
    print(f"case 2 {result} == 1")


def case3(solution: Solution) -> None:
    stockPrices: list[list[int]] = [[36,9],[17,93],[34,4],[30,11],[11,41],[53,36],[5,92],[81,92],[28,36],[3,45],[72,33],[64,1],[4,70],[16,73],[99,20],[49,33],[47,74],[83,91]]
    result: int = solution.minimumLines(stockPrices) 
    print(f"case 3 {result} == 17")


def case4(solution: Solution) -> None:
    stockPrices: list[list[int]] = [[1,1],[500000000,499999999],[1000000000,999999998]]
    result: int = solution.minimumLines(stockPrices) 
    print(f"case 4 {result} == 2")


def main() -> None:
    print("2280. Minimum Lines to Represent a Line Chart")

    solution = Solution()

    case1(solution)
    case2(solution)
    case3(solution)
    case4(solution)


if __name__ == "__main__":
    main()