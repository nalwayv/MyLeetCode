def processStr(s: str) -> str:
    """
    Rules:
        -'*' removes the last character from result, if it exists.
        -'#' duplicates the current result and appends it to itself.
        -'%' reverses the current result.
    """
    stack: list[str] = []
    
    for ch in s:
        if ch in "*#%":
            if ch == "*" and stack:
                stack.pop()

            if ch == "#":
                n: int = len(stack)
                for i in range(n):
                    stack.append(stack[i])

            if ch == "%":
                stack.reverse()
        else:
            stack.append(ch)

    return "".join(stack)


def main() -> None:
    print("3612. Process String with Special Operations I")

    print(f"a#b%*\t= {processStr("a#b%*")}")
    print(f"z*#\t= {processStr("z*#")}")
    print(f"a###\t= {processStr("a###")}")
    print(f"ztv#*l\t= {processStr("ztv#*l")}")


if __name__ == "__main__":
    main()