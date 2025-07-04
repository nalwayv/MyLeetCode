class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        p1: int = 0
        end: int = len(arr)

        while p1 < end:
            p2 = p1
            count: int = 0

            while p2 < end and (arr[p2] & 1) != 0:
                count += 1
                p2 += 1

                if count == 3:
                    return True
            
            p1 = p2 + 1

        return False


def main() -> None:
    sol = Solution()
    print(sol.threeConsecutiveOdds([2,6,4,1])) # false
    print(sol.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))# true
    print(sol.threeConsecutiveOdds([2,4,8,10,12,14,15,17,19,22,24,28]))# true
    print(sol.threeConsecutiveOdds([2,2,2,2,2,2,2,2,2,1,1,1])) # true
    print(sol.threeConsecutiveOdds([424,915,193,591,923])) # true


if __name__ == "__main__":
    main()