def numberOfSubstrings(s: str) -> int:
    freq: dict[str, int] = {abc: 0 for abc in "abc"}
    count: int = 0
    
    length: int = len(s)
    p1: int = 0

    for p2 in range(length):
        if s[p2] not in "abc":
            continue

        freq[s[p2]] += 1

        # Check if we have at least one of each character
        while freq["a"] and freq["b"] and freq["c"]:
            # all substrings starting from p1 to the end of the string are valid
            count += length- p2

            # update frequency and move pointer
            freq[s[p1]] -= 1
            p1 += 1

    return count


def main() -> None:
    print("1358. Number of Substrings Containing All Three Characters")

    count: int = numberOfSubstrings("abcabc")
    # valid substrings: abc, abca, abcab, abcabc, bca, bcab, bcabc, cab, cabc, abc
    print(f"Result: {count}")


if __name__ == "__main__":
    main()