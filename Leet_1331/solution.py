class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if not arr:
            return arr
        
        arr_sorted: list[int] = sorted(arr)
        
        table: dict[int, int] = {}
        table[arr_sorted[0]] = 1
        
        n: int = len(arr)
        rank: int = 1
        
        for idx in range(1, n):
            curr: int = arr_sorted[idx]
            prev: int = arr_sorted[idx-1]

            if curr not in table:
                table[curr] = 0
            
            if curr == prev:
                table[curr] = rank
            else:
                rank += 1
                table[curr] = rank

        for idx, val in enumerate(arr):
            arr[idx] = table[val]

        return arr
        

def main() -> None:
    print("1331. Rank Transform of an Array")

    sol = Solution()

    # arr: list[int] = [40,10,20,30]
    # arr: list[int] = [100, 100, 100]
    arr: list[int] = [37,12,28,9,100,56,80,5,12]
    
    print(sol.arrayRankTransform(arr))


if __name__ == "__main__":
    main()