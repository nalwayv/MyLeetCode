class Solution:
    def generate(self, result: list[str], builder: str, n: int):
        if len(builder) == n:
            result.append(builder)
            return
        
        self.generate(result, builder + '1', n)

        if not builder or builder[-1] != '0':
            self.generate(result, builder + '0', n)

    def validStrings(self, n: int) -> list[str]:
        result: list[str] = []
        self.generate(result, "", n)

        return result


def main() -> None:
    print("3211. Generate Binary Strings Without Adjacent Zeros")

    sol = Solution()
    
    print(sol.validStrings(n= 3))
    print(sol.validStrings(n= 1))


if __name__ == "__main__":
    main()