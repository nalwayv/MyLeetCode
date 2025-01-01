class Solution:
    def maxScore(self, s: str) -> int:
        n: int = len(s)
        left: list[int] = [0] * n
        right: list[int] = [0] * n
        
        # prefix sum 0 left to right
        left[0] = 1 if s[0] == "0" else 0
        for i in range(1, n):
            current: int = 1 if s[i] == "0" else 0
            left[i] = left[i-1] + current

        # prefix sum 1 right to left
        right[0] = 1 if s[n-1] == "1" else 0
        for i in range(1, n):
            current: int = 1 if s[n-i-1] == "1" else 0
            right[i] = right[i-1] + current

        result: int = -1
        for i in range(1, n):
            result = max(result, left[i-1] + right[n-i-1])

        return result


def main() -> None:
    print("1422. Maximum Score After Splitting a String")
    
    sol = Solution()

    print(f"case 1: {"pass" if sol.maxScore("011101") == 5 else "fail"}")
    print(f"case 2: {"pass" if sol.maxScore("00111") == 5 else "fail"}")
    print(f"case 3: {"pass" if sol.maxScore("1111") == 3 else "fail"}")


if __name__ == "__main__":
    main()