class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Given a sentence that consists of some words separated by a single space, 
        and a searchWord, check if searchWord is a prefix of any word in sentence.

        Args:
            sentence (str):
            searchWord (str):

        Returns:
            index of first word in sentence to match prefix searchWord
        """
        words: list[str] = sentence.split(" ")
        m: int = len(searchWord)

        for i, word in enumerate(words):
            n: int = len(word)
            if n >= m and word[:m] == searchWord:
                return i + 1
        
        return -1


def main() -> None:
    print("1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence")
    
    sol = Solution()
    print(sol.isPrefixOfWord("i love eating burger, bunger", "burg") == 4)
    print(sol.isPrefixOfWord("this problem is an easy problem", "pro") == 2)
    print(sol.isPrefixOfWord("i am tired", "you") == -1)


if __name__ == "__main__":
    main()