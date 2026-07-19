def smallest_subsequence(s: str) -> str:
    """Return the lexicographically smallest subsequence of s containing only distinced characters.

    Args:
        s(str): a lowercase string containing character from a to z.

    Returns:
        str: the lexicographically smallest subsequence of s containing only distinced characters.
    """
    def idx(ch: str) -> int:
        """helper to convert to index between 0 and 25"""
        return ord(ch) - ord("a")

    ch_index: dict[str, int] = {ch: i for i, ch in enumerate(s)}
    seen: list[bool] = [False] * 26
    stack: list[str] = []
    for i, ch in enumerate(s):

        if seen[idx(ch)]:
            continue

        # - maintain a monotonic stack
        # - ensure that the character at the top of the stack will appear later
        while stack and ch < stack[-1] and ch_index[stack[-1]] > i:
            seen[idx(stack[-1])] = False
            _ = stack.pop()

        stack.append(ch)
        seen[idx(ch)] = True

    return "".join(stack)


def main() -> None:
    print("1081. Smallest Subsequence of Distinct Characters")

    s: str = "bcabc"
    result: str = "pass" if smallest_subsequence(s) == "abc" else "fail"
    print(f"{s} should equal 'abc' ? {result}")


if __name__ == "__main__":
    main()
