class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        nums: list[int] = []

        for i in range(1, n+1):
            p: int = pow(i, x)
            if p <= n:
                nums.append(p)

        mod: int = int(1e9+7)
        dp: list[int] = [0] * (n + 1)
        dp[0] = 1

        for num in nums:
            for i in range(n, num - 1, -1):
                dp[i] = (dp[i] + dp[i - num]) % mod
        
        return dp[n] % int(1e9+7)


def main() -> None:
    print("2787. Ways to Express an Integer as Sum of Powers")

    sol = Solution()
    print(sol.numberOfWays(n=10, x=2))
    print(sol.numberOfWays(n=4, x=1))


if __name__ == "__main__":
    main()