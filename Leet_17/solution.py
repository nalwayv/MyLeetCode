class Solution:
    def __init__(self) -> None:
        self.table: dict[str,str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def backtrack(self, result: list[str], current: list[str], digits: str, idx: int) -> None:
        if idx == len(digits):
            result.append("".join(current))
            return
        
        for digit in self.table[digits[idx]]:
            current.append(digit)
            self.backtrack(result, current, digits, idx+1)
            current.pop()

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        result: list[str] = []
        current: list[str] = []

        self.backtrack(result, current, digits, 0)
        return result


def main() -> None:
    print("17. Letter Combinations of a Phone Number")
    
    sol = Solution()
    
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations("2"))
    print(sol.letterCombinations(""))


if __name__ == "__main__":
    main()