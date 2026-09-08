def distinctSubseqII(s: str) -> int:
    """
    Return the number of distinct non-empty subsequences of s
    """
    mod: int = 1000000007

    n: int = len(s)
    dp: list[int] = [0] * (n + 1)
    dp[0] = 1

    seen: dict[str, int] = {}

    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]

        curr: str = s[i - 1]
        if curr in seen:
            dp[i] -= dp[seen[curr] - 1]
        seen[curr] = i
        
    return (dp[n] - 1) % mod


def main() -> None:
    print("940. Distinct Subsequences II")
    result:str = "pass" if distinctSubseqII("abc") == 7 else "fail"
    print(f"Result for abc should equal 7 ? {result}")


if __name__ == "__main__":
    main()