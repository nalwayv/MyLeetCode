class Solution:
    def reverse(self, s: str, lo: int, hi: int) -> str:
        if hi >= len(s):
            hi = len(s) - 1

        result: list[str] = [ch for ch in s]
        while lo < hi:
            result[lo], result[hi] = result[hi], result[lo]
            lo += 1
            hi -= 1
            
        return "".join(result)

    def reverseStr(self, s: str, k: int) -> str:
        """
        Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
        
        Rules:
            - If there are fewer than k characters left, reverse all of them. 
            - If there are less than 2k but greater than or equal to k characters, then reverse the first k characters.

        Args:
            s (str): word to reverse.
            k (int): amount of characters in each 2k to swap.
        
        Returns:
            str: reversed s following rules.
        """

        n: int = len(s)
        two_k: int = 2 * k
        if n <= k:
            return self.reverse(s, 0, len(s) - 1)

        result: str = ""
        p1: int = 0
        while p1 < n:
            p2: int = p1 + two_k
            s2: str = s[p1:p2]
            result += self.reverse(s2, 0, k-1)
            p1 = p2

        return "".join(result)


def test_case(sol: Solution, s: str, expected: str, k: int) -> None:
    reverse: str = sol.reverseStr(s, k)
    result: str = "pass" if reverse == expected else "fail"
    print(f"Test case {s} = {result}")


def main() -> None:
    print("541. Reverse String II")
    
    sol = Solution()
    test_case(sol, "abcdefg", "bacdfeg", 2)
    test_case(sol, "onetwoten", "enotwonet", 3)
    test_case(sol, "abcd", "bacd", 2)


if __name__ == "__main__":
    main()