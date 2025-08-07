class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        def check(val: int):
            count: int = 1
            prev: int = position[0]

            for curr in position[1:]:
                if curr - prev >= val:
                    count += 1
                    prev = curr

                    if count == m:
                        return True

            return False
    
        position.sort()
        
        n: int = len(position)
        lo: int = 1
        hi: int = position[n-1] - lo
        result: int = 0

        while lo <= hi:
            mid: int = (lo + hi) // 2

            if check(mid):
                result = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return result


def main() -> None:
    print("1552. Magnetic Force Between Two Balls")

    sol = Solution()
    
    print(sol.maxDistance(position = [1,2,3,4,7], m = 3)) # 3
    print(sol.maxDistance(position = [5,4,3,2,1,1000000000], m = 2)) # 999999999
    print(sol.maxDistance(position = [79,74,57,22], m = 4)) # 5


if __name__ == "__main__":
    main()