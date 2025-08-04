class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        if len(edges) < 2:
            return -1
        return (set(edges[0]) & set(edges[1])).pop()
    

def main() -> None:
    print("1791. Find Center of Star Graph")
    sol = Solution()

    case_1: int = sol.findCenter([[1,2], [2,3], [4,2]])
    print(f"case 1 should equal 2? {case_1}")

    case_2: int = sol.findCenter([[1,2],[5,1],[1,3],[1,4]])
    print(f"case 2 should equal 1? {case_2}")
    

if __name__ == "__main__":
    main()