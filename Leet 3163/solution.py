class Solution:
    def compressedString(self, word: str) -> str:
        """Compress sting following rules.
        
        - Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
        
        Meaning a word like aaaaaaaaaaaa becomes 9a3a.
        
        Args:
            word (str): word to compress.
        
        Returns:
            compressed string
        """
        p1: int = 0
        p2: int = 0
        n: int = len(word)
        comp: list[str] = []

        while p1 < n:
            p2 = p1
            while p2 < n and word[p1] == word[p2]:
                p2 += 1

            diff: int = p2 - p1
            if diff > 0:
                if diff > 8:
                    #loop breaks down diff into chunks of 9
                    #and what else if left.
                    #>>>example:
                    #ddddddddddddddddddddddddd
                    #9d9d7d
                    while diff > 0:
                        min_diff: int = min(diff, 9)
                        comp.append(f"{min_diff}{word[p1]}")
                        diff -= 9
                else:
                    comp.append(f"{diff}{word[p1]}")
            p1 = p2

        return "".join(comp)


def case1(solution: Solution) -> None:
    test: bool = solution.compressedString("abcde") == "1a1b1c1d1e"
    print(f"case 1: { "pass" if test else "fail" }")


def case2(solution: Solution) -> None:
    test: bool = solution.compressedString("aaaaaaaaaaaaaabb") == "9a5a2b"
    print(f"case 2: { "pass" if test else "fail" }")


def case3(solution: Solution) -> None:
    test: bool = solution.compressedString("aaaaaaaaay") == "9a1y"
    print(f"case 2: { "pass" if test else "fail" }")


def main() -> None:
    print("3163. String Compression III")
    
    solution = Solution()
    
    case1(solution)
    case2(solution)
    case3(solution)


if __name__ == "__main__":
    main()