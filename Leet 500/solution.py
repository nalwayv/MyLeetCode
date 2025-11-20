class Solution:
    def contains_word(self, word: str, letters: set[str]):
        for ch in word:
            if ch not in letters:
                return False
        return True

    def findWords(self, words: list[str]) -> list[str]:
        row1 = set([c for c in 'qwertyuiop'])
        row2 = set([c for c in 'asdfghjkl'])
        row3 = set([c for c in 'zxcvbnm'])

        result: list[str] = []
        for word in words:
            if self.contains_word(word.lower(), row1) or self.contains_word(word.lower(), row2) or self.contains_word(word.lower(), row3):
                result.append(word)

        return result


def main() -> None:
    print('500. Keyboard Row')

    solution = Solution()

    case1: list[str] = solution.findWords(['Hello','Alaska','Dad','Peace'])
    print(case1)

    case2: list[str] = solution.findWords(['omk'])
    print(case2)

    case3: list[str] = solution.findWords(['adsdf','sfd'])
    print(case3)


if __name__ == '__main__':
    main()