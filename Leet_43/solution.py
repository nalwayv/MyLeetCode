class Solution:
    def __init__(self) -> None:
        self._look_up: dict[str, int] = {
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
    
    def _construct_int(self, num: str) -> int:
        result: int = 0
        for n in num:
            if n in self._look_up:
                result *= 10
                result += self._look_up[n]
        return result

    def multiply(self, num1: str, num2: str) -> str:
        return f"{self._construct_int(num1) * self._construct_int(num2)}"
    

def main() -> None:
    print("43. Multiply Strings")

    sol = Solution()

    case1: str = sol.multiply("2", "3")
    print(f"case 1: { "pass" if case1 == "6" else "fail" }")

    case2: str = sol.multiply("123", "456")
    print(f"case 2: { "pass" if case2 == "56088" else "fail" }")



if __name__ == "__main__":
    main()