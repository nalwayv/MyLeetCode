class Solution:
    def _skip_white_space(self, s: str) -> int:
        p1: int = 0
        n: int = len(s)
        while p1 < n and s[p1].isspace():
            p1 += 1
        return p1
    
    def _clamp(self, val: int, lo: int, hi: int) -> int:
        if val >= hi: 
            return hi
        if val <= lo: 
            return lo
        return val
    
    def myAtoi(self, s: str) -> int:
        MAX_VALUE: int = 2147483647
        MIN_VALUE: int = -2147483648

        n: int = len(s)
        if n == 0:
            return 0
        
        p1: int = self._skip_white_space(s)
        if p1 == n or s[p1].isalpha() or s[p1] == ".":
            return 0

        possible_numbers: list[str] = []
        while p1 < n:
            if s[p1].isnumeric() or s[p1] in ["-", "+"]:
                p2: int = p1 + 1
                while p2 < n and s[p2].isnumeric():
                    p2 += 1

                possible_numbers.append(s[p1:p2])

                p1 = p2 + 1
            else:
                p1 += 1
        
        result: int = 0
        if len(possible_numbers) > 0:
            try:
                result = self._clamp(int(possible_numbers[0]), MIN_VALUE, MAX_VALUE)
            except ValueError:
                result = 0
        return result


def main() -> None:
    print("8. String to Integer (atoi)")
    
    sol = Solution()

    print(sol.myAtoi("42"))
    print(sol.myAtoi("   -042"))
    print(sol.myAtoi("1337c0d3"))
    print(sol.myAtoi("0-1"))
    print(sol.myAtoi("words and 987"))
    print(sol.myAtoi("-91283472332"))
    print(sol.myAtoi(" "))


if __name__ == "__main__":
    main()