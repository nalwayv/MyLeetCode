def reverseParentheses(s: str) -> str:
    builder: list[str] = []
    for ch in s:
        if ch == ")":
            word: str = ""
            while builder and builder[-1] != "(":
                word = builder.pop() + word
            _ = builder.pop()
            builder.append(word[::-1])
        else:
            builder.append(ch)
    return "".join(builder)


def main() -> None:
    print(reverseParentheses("(ed(et(oc))el)"))

if __name__ == "__main__":
    main()