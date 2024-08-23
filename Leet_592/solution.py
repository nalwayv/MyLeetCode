import math
import re

class Solution:
    def parse(self, exp: str) -> list[int]:
        split: list[str] = re.split(r"/|(?=[-+])", exp)
        result: list[int] = [int(s) for s in split if len(s) != 0]
        return result
    
    def fractionAddition(self, expression: str) -> str:
        parsed: list[int] = self.parse(expression)
        n: int = len(parsed)

        # get lcm denominator
        den: int = 1
        for i in range(0, n, 2):
            den *= parsed[i+1] // math.gcd(den, parsed[i+1])
        
        num: int = 0
        for i in range(0, n, 2):
            n: int = parsed[i]
            d: int = parsed[i+1]

            # multiply numerator by how many times 
            # denominator goes into lcm
            num += n * (den//d)

        # get irreducible fraction
        gcd: int = math.gcd(num, den)

        num //= gcd
        den //= gcd

        return f"{num}/{den}"


def main() -> None:
    print("592. Fraction Addition and Subtraction")

    sol = Solution()

    expression_1: str = "-1/2+1/2"
    expression_2: str = "-1/2+1/2+1/3"
    expression_3: str = "1/3-1/2"
    expression_4: str = "+5/6-2/3+4/7"
    expression_5: str = "-10/2+10/7-2/7"

    print(sol.fractionAddition(expression_1) == "0/1")
    print(sol.fractionAddition(expression_2) == "1/3")
    print(sol.fractionAddition(expression_3) == "-1/6")
    print(sol.fractionAddition(expression_4) == "31/42")
    print(sol.fractionAddition(expression_5) == "-27/7")


if __name__ == "__main__":
    main()