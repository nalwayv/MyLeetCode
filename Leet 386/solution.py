class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        nums: list[int] = [i for i in range(1, n+1)]
        nums.sort(key=str)
        return nums
    

def main() -> None:
    print("386. Lexicographical Numbers")

    sol = Solution()
    ln: list[int] = sol.lexicalOrder(13)
    
    print("[", end="")
    for num in ln:
        print(f" {num} ", end="")
    print("]")


if __name__ == "__main__":
    main()