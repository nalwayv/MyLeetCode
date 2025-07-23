class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Given a string s and two integers x and y. You can perform two types of operations any number of times.

        - Remove substring "ab" and gain x points.
        - Remove substring "ba" and gain y points.

        Return the maximum points you can gain after applying the above operations on s.
        """
        # check for BA then AB
        # else check for AB then BA

        score: int = 0
        if x < y:
            stk: list[str] = []
            for ch in s:
                if stk and stk[-1] == "b" and ch == "a":
                    score += y
                    stk.pop()
                else:
                    stk.append(ch)

            s = "".join(stk)
            stk.clear()

            for ch in s:
                if stk and stk[-1] == "a" and ch == "b":
                    score += x
                    stk.pop()
                else:
                    stk.append(ch)
        else:
            stk: list[str] = []
            for ch in s:
                if stk and stk[-1] == "a" and ch == "b":
                    score += x
                    stk.pop()
                else:
                    stk.append(ch)

            s = "".join(stk)
            stk.clear()

            for ch in s:
                if stk and stk[-1] == "b" and ch == "a":
                    score += y
                    stk.pop()
                else:
                    stk.append(ch)
    
        return score


def main() -> None:
    print("1717. Maximum Score From Removing Substrings")

    sol = Solution()
    
    print("case 1")
    print(sol.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))
    
    print("case 2")
    print(sol.maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4))


if __name__ == "__main__":
    main()