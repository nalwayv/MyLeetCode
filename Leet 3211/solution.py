class Solution:
    def generate(self, builder: list[str], result: list[str], n: int = 0, k: int = 0) -> None:
        if n < 1:
            # check if valid
            for i in range(0, len(builder)-1):
                if builder[i] == '0' and builder[i+1] == '0':
                    return
            
            result.append("".join(builder))

            return
        
        for i in range(k):
            tmp: str = builder[n-1]

            builder[n - 1] = str(i)
            self.generate(builder, result, n - 1, k)
            builder[n - 1] = tmp


    def validStrings(self, n: int) -> list[str]:
        builder: list[str] = ['0' for _ in range(n)]
        result: list[str] = []
        
        self.generate(builder, result, n, 2)

        return result


def main() -> None:
    print("3211. Generate Binary Strings Without Adjacent Zeros")

    sol = Solution()
    
    print(sol.validStrings(n= 3))
    print(sol.validStrings(n= 1))


if __name__ == "__main__":
    main()