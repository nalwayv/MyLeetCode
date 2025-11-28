class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        result: list[int] = [0] * len(s)
        c_at: list[int] = [i for i in range(len(s)) if s[i] == c]

        # left
        for i in range(c_at[0], -1, -1):
            result[i] = abs(c_at[0] - i)
        
        # right
        for i in range(c_at[-1], len(s)):
            result[i] = abs(c_at[-1] - i)
        
        # middle
        for p in range(len(c_at) - 1):
            p1: int = c_at[p]
            p2: int = c_at[p+1]
            i: int = 0
            while p1 <= p2:
                result[p1] = result[p2] = i
                i += 1
                p1 += 1
                p2 -= 1
                
        return result


def main() -> None:
    print('821. Shortest Distance to a Character')
    sol = Solution()
    case1_result: list[int] = sol.shortestToChar('loveleetcode', 'e')
    print(case1_result)


if __name__ == '__main__':
    main()