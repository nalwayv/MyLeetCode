def detect_capital_use(word: str) -> bool:
    """
    Detect if the usage of capital letters in word follows one of these rules.

    - All letters in this word are capital.
    - All letters in this word are not capitals.
    - Only the first letter in this word is capital.

    Args:
        word (str): a word consists of lowercase and uppercase English letters.
        word length is between 1 - 100

    Returns:
        bool: true if the usage of capitals follows one of these rules.
    """
    if len(word) < 1 or len(word) > 100:
        return False

    count: int = 0
    for w in word:
        if 0 <= ord(w) - ord("A") <= 25:
            count += 1

    # all letters are uppercase
    if count == len(word):
        return True

    # all letters are lowercase
    if count == 0:
        return True

    # only the first letter in word is uppercase
    if count == 1 and (0 <= ord(word[0]) - ord("A") <= 25):
        return True

    return False


def test_case(word: str, expected: bool):
    bool_str: str = "true" if expected else "false"
    result: str = "pass" if detect_capital_use(word) == expected else "fail"
    print(f"detect_capital_use('{word}') should equal {bool_str}? {result}")


def main() -> None:
    print("520. Detect Capital")

    test_case("USA", True)
    test_case("leetcode", True)
    test_case("Google", True)
    test_case("flaG", False)


if __name__ == "__main__":
    main()
