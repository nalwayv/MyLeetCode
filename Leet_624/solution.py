class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        first_pass: bool = True
        max_diff: int = -1
        prev_lo: int = -1
        prev_hi: int = -1
        diffs: list[int] = [0] * 5

        for arr in arrays:
            lo: int = arr[0]
            hi: int = arr[len(arr) - 1]
            if first_pass:
                prev_lo = lo
                prev_hi = hi
                first_pass = False
            else:
                diffs[0] = abs(prev_lo - lo)
                diffs[1] = abs(prev_lo - hi)
                diffs[2] = abs(prev_hi - lo)
                diffs[3] = abs(prev_hi - hi)
                diffs[4] = max_diff

                max_diff = max(diffs)
                prev_lo = min(lo, prev_lo)
                prev_hi = max(hi, prev_hi)

        return max_diff
    

def main() -> None:
    print("624. Maximum Distance in Arrays")
    
    sol = Solution()

    arrays_a = [[1,2,3],[4,5],[1,2,3]]
    max_dis_a = sol.maxDistance(arrays_a)
    print(max_dis_a == 4)

    arrays_b = [[1],[1]]
    max_dis_b = sol.maxDistance(arrays_b)
    print(max_dis_b == 0)
            
    arrays_c = [[1],[2],[3,4,5],[6,7,8]]
    max_dis_c = sol.maxDistance(arrays_c)
    print(max_dis_c == 7)

    arrays_d = [[8,9],[1,2],[5,6]]
    max_dis_d = sol.maxDistance(arrays_d)
    print(max_dis_d == 8)

    arrays_e = [[6,7,8],[0,2,4],[0,4,9]] 
    max_dis_e = sol.maxDistance(arrays_e)
    print(max_dis_e == 9)

    arrays_f = [[-1,5,11],[6,10]]
    max_dis_f = sol.maxDistance(arrays_f)
    print(max_dis_f == 11)


if __name__ == "__main__":
    main()