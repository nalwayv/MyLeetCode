class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count: int = 0
        for word in text.split(' '):
            check_brocken_letters: str = ''.join('*' if ch in brokenLetters else ch for ch in word)
            
            if word == check_brocken_letters:
                count += 1

        return count


def main() -> None:
    print('1935. Maximum Number of Words You Can Type')

    solution = Solution()

    case_1: int = solution.canBeTypedWords(text='hello world', brokenLetters='ad')
    print(f'case 1 should equal 1? {case_1}')

    case_2: int = solution.canBeTypedWords(text='leet code', brokenLetters='lt')
    print(f'case 2 should equal 1? {case_2}')

    case_3: int = solution.canBeTypedWords(text='leet code', brokenLetters='e')
    print(f'case 3 should equal 0? {case_3}')


if __name__ == '__main__':
    main()