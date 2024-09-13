class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n: int = len(queries)
        result: list[int] = [0]*n
        table: dict[str, int] = {}

        for i in range(n):
            start: int = queries[i][0]
            end: int = queries[i][1]+1

            h: str = f"[{start},{end}]"

            if h in table:
                result[i] = table[h]
            else:
                x: int = 0
                for j in range(start, end):
                    x ^= arr[j]
                    
                result[i] = x
                table[h] = x
                
        return result
    

def main() -> None:
    print("1310. XOR Queries of a Subarray")
    sol = Solution()
    arr: list[int] = [1,3,4,8]
    queries: list[list[int]] = [[0,1],[1,2],[0,3],[3,3]]
    result: list[int] = sol.xorQueries(arr, queries)
    print(result)


if __name__ == "__main__":
    main()