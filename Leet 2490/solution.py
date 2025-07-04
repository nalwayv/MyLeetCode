class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """Check if sentence is a circular sentence

        A sentence is circular if:
            - The last character of a word is equal to the first character of the next word.
            - The last character of the last word is equal to the first character of the first word.
        
        Args:
            sentence (string): check if its circular

        Returns:
            true if sentence is circular
        """
        if len(sentence) == 0:
            return False
        
        #check the last character of a word is equal to 
        #the first character of the next word.        
        if sentence[0] != sentence[-1]:
            return False
        
        split: list[str] = sentence.split(" ")

        for i in range(1, len(split)):
            first: str = split[i-1]
            second: str = split[i]

            #check last character of the last word is equal to
            #the first character of the first word
            if first[-1] != second[0]:
                return False
            
        return True


def main() -> None:
    print("2490. Circular Sentence")

    sol = Solution()

    case_1: bool = sol.isCircularSentence("leetcode exercises sound delightful")
    print(f"case_1: { "pass" if case_1 else "fail" }")
    
    case_2: bool = sol.isCircularSentence("eetcode")
    print(f"case_2: { "pass" if case_2 else "fail" }")

    case_3: bool = sol.isCircularSentence("Leetcode is cool")
    print(f"case_2: { "pass" if not case_3 else "fail" }")

    case_4: bool = sol.isCircularSentence("A")
    print(f"case_4: { "pass" if case_4 else "fail" }")


if __name__ == "__main__":
    main()