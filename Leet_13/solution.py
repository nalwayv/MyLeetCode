class Solution:
    """
    13. Roman to Integer
    """
    def test_I(self, a: str, b: str) -> bool:
        return a == "I" and (b == "V" or b == "X")
    
    def test_X(self, a: str, b: str) -> bool:
        return a == "X" and (b == "L" or b == "C")
    
    def test_C(self, a: str, b: str) -> bool:
        return a == "C" and (b == "D" or b == "M")
    
    def romanToInt(self, s: str) -> int:
        symbols: dict[str, int] = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" : 1,
        }
        
        num: int = 0
        p1: int = len(s) - 1

        while p1 >= 0:
            sym1: str = s[p1]

            if p1 - 1 >= 0:
                sym2: str = s[p1 - 1]
                
                if self.test_I(sym2, sym1) or self.test_X(sym2, sym1) or self.test_C(sym2, sym1):
                    num += symbols[sym1] - symbols[sym2]
                    p1 -= 2
                else:
                    num += symbols[sym1]
                    p1 -= 1
            else:
                num += symbols[sym1]
                p1 -= 1

        return num


def case1(solution: Solution) -> None:
    input: str = "III"
    result: int = solution.romanToInt(input)
    print(f"({input})=3 ? {result == 3}")


def case2(solution: Solution) -> None:
    input: str = "LVIII"
    result: int = solution.romanToInt(input)
    print(f"({input})=58 ? {result == 58}")


def case3(solution: Solution) -> None:
    input: str = "MCMXCIV"
    result: int = solution.romanToInt(input)
    print(f"({input})=1994 ? {result == 1994}")


def case4(solution: Solution) -> None:
    input: str = "IV"
    result: int = solution.romanToInt(input)
    print(f"({input})=4 ? {result == 4}")


def main() -> None:
    solution = Solution()
    
    case1(solution)
    case2(solution)
    case3(solution)
    case4(solution)


if __name__ == "__main__":
    main()