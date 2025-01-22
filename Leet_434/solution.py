class Solution:
    def countSegments(self, s: str) -> int:
        lo: int = 0
        hi: int = 0
        n: int = len(s)
        
        count: int = 0

        while lo < n:
            hi = lo
            while hi < n and s[hi] != ' ':
                hi += 1

            if hi - lo > 0:
                count += 1

            while hi < n and s[hi] == ' ':
                hi += 1

            lo = hi

        return count


def main() -> None:
    print("434. Number of Segments in a String")
    
    sol = Solution()
    
    case_1: int = sol.countSegments("Hello, my name is John")
    print(f"{case_1} == 5")

    case_2: int = sol.countSegments("Hello")
    print(f"{case_2} == 1")

    case_3: int = sol.countSegments("                ")
    print(f"{case_3} == 0")


if __name__ == "__main__":
    main()