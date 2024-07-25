class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        """ check if s is a palindrome
        """
        def alphanumeric_only(s: str) -> str:
            """ remove all other characters except alphanumeric
            """
            n: int = len(s)
            p1: int = 0
            
            result: list[str] = []

            while p1 < n:
                p2: int = p1
                while p2 < n and s[p2].isalnum():
                    p2 += 1

                if p1 != p2:
                    result.append(s[p1:p2].lower())

                p1 = p2 + 1
        
            return "".join(result)
        
        text: str = alphanumeric_only(s)
        p1: int = 0
        p2: int = len(text)-1

        while p1 < p2:
            if text[p1] != text[p2]:
                return False

            p1 += 1
            p2 -= 1

        return True


def example1(sol: Solution):
    check: bool = sol.isPalindrome("A man, a plan, a canal: Panama")
    print(f"Example 1: 'A man, a plan, a canal: Panama' ? {check}")


def example2(sol: Solution):
    check: bool = sol.isPalindrome("race a car")
    print(f"Example 2: 'race a car' ? {check}")


def example3(sol: Solution):
    check: bool = sol.isPalindrome(" ")
    print(f"Example 3: ' ' ? {check}")


def main() -> None:
    print("125. Valid Palindrome")

    solution = Solution()

    example1(solution)
    example2(solution)
    example3(solution)


if __name__ == "__main__":
    main()
