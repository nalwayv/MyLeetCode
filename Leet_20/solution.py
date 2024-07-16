class Solution:
    def isValid(self, s: str) -> bool:
        stk: list[str] = []

        for ch in s:
            if ch in ["(", "[", "{"]:
                stk.append(ch)
            else:
                if not stk:
                    return False
                
                current: str = stk.pop()
                if current == "(" and ch != ")":
                    return False
                
                if current == "[" and ch != "]":
                    return False
                
                if current == "{" and ch != "}":
                    return False

        return True if not stk else False


def main() -> None:
    solution = Solution()
    print(f"Expect: True, Output: {solution.isValid("((()()))")}")
    print(f"Expect: True, Output: {solution.isValid("(((11)()))")}")
    print(f"Expect: True, Output: {solution.isValid("(){}[]")}")
    print(f"Expect: False, Output: {solution.isValid("([)")}")


if __name__ == "__main__":
    main()