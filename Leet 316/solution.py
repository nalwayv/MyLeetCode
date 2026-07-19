def remove_duplicate_letters(s: str) -> str:
    """Remove duplicate letters from s and return the result in lexicographical order.

    Args:
        s (str): a lowercase string containing letters from a to z.

    Returns:
        str: 's' with duplicates removed and in lexicographical order.
    """
    def idx(ch: str) -> int:
        return ord(ch) - ord("a")

    fr: dict[str, int] = {}
    for ch in s:
        fr[ch] = fr.get(ch, 0) + 1

    seen: list[bool] = [False] * 26
    stack: list[str] = []
    for ch in s:
        fr[ch] -= 1

        if seen[idx(ch)]:
            continue

        # maintain a monotonic stack
        while stack and ch < stack[-1] and fr[stack[-1]] > 0:
            seen[idx(stack[-1])] = False
            _ = stack.pop()

        stack.append(ch)
        seen[idx(ch)] = True

    return "".join(stack)


def main() -> None:
    print("316. Remove Duplicate Letters")

    s: str = "bcabc"
    result: str = "pass" if remove_duplicate_letters(s) == "abc" else "fail"
    print(f"{s} should equal 'abc' ? {result}")


if __name__ == "__main__":
    main()
