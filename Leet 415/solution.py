class Solution:
    def __init__(self) -> None:
        self.to_int: dict[str, int] = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        self.to_str: dict[int, str] = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9"
        }

    def _convert_to_int(self, num: str) -> int:
        value: int = 0
        for n in num:
            val: int = self.to_int[n]
            value *= 10
            value += val
        return value
    
    def addStrings(self, num1: str, num2: str) -> str:
        total: int = self._convert_to_int(num1) + self._convert_to_int(num2)
        if total == 0:
            return "0"
        
        # breakdown
        stk: list[int] = []
        while total > 0:
            val: int = total % 10
            total //= 10
            stk.append(val)

        # str builder
        result: list[str] = []
        while stk:
            result.append(self.to_str[stk.pop()])
        return "".join(result)
    

def main() -> None:
    print("415. Add Strings")

    sol = Solution()
    
    print(sol.addStrings("11", "123"))
    print(sol.addStrings("456", "77"))
    print(sol.addStrings("0", "0"))
    print(sol.addStrings("1", "9"))


if __name__ == "__main__":
    main()

    