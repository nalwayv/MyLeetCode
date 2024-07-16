class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal:list[list[int]] = []

        for i in range(1, numRows+1):
            numbers: list[int] = []
            num: int = 1
            for j in range(1, i+1):
                print(f"I: {i} J: {j} Num: {num}")
                numbers.append(num)
                num = num * (i-j) // j
            print("-"*5)
            pascal.append(numbers)

        return pascal

def main() -> None:
    solution = Solution()
    print(f"Output: {solution.generate(5)}")
    print(f"Output: {solution.generate(1)}")

if __name__ == "__main__":
    main()