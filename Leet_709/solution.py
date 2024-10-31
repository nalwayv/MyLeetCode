class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
    

def main() -> None:
    print("709. To Lower Case")
    sol = Solution()
    before: str = "Hello"
    after: str = sol.toLowerCase("Hello")
    print(f"{before} -> {after}")


if __name__ == "__main__":
    main()