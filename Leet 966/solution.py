class Solution:
    def _mask_vowels(self, word: str) -> str:
        return ''.join('*' if ch in 'aeiouAEIOU' else ch for ch in word)
    
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        unique_words: set[str] = set(wordlist)
        case_insensitive: dict[str, str] = {}
        vowel_insensitive: dict[str, str] = {}

        for word in wordlist:
            case_key: str = word.lower()
            vowel_key: str = self._mask_vowels(case_key)
            
            case_insensitive.setdefault(case_key, word)
            vowel_insensitive.setdefault(vowel_key, word)
            # if case_key not in case_insensitive:
            #     case_insensitive[case_key] = word

            # if vowel_key not in vowel_insensitive:
            #     vowel_insensitive[vowel_key] = word

        result: list[str] = []
        for query in queries:
            if query in unique_words:
                result.append(query)
            elif (key := query.lower()) in case_insensitive:
                result.append(case_insensitive[key])
            elif (key := self._mask_vowels(query.lower())) in vowel_insensitive:
                result.append(vowel_insensitive[key])
            else:
                result.append('')

        return result


def case_1(solution: Solution) -> None:
    print('case 1')
    wordlist = ['KiTe','kite','hare','Hare']
    queries = ['kite','Kite','KiTe','Hare','HARE','Hear','hear','keti','keet','keto']
    # expect ['kite','KiTe','KiTe','Hare','hare','','','KiTe','','KiTe']
    for r in solution.spellchecker(wordlist, queries):
        print(r)


def case_2(solution: Solution) -> None:
    print('case 2')
    wordlist = ['yellow']
    queries = ['YellOw']
    # expect ['yellow']
    for r in solution.spellchecker(wordlist, queries):
        print(r)


def case_3(solution: Solution) -> None:
    print('case 3')
    wordlist = ['zeo','Zuo']
    queries = ['zuo']
    # expect ['Zuo']
    for r in solution.spellchecker(wordlist, queries):
        print(r)


def main() -> None:
    print('966. Vowel Spellchecker')

    solution = Solution()
    
    case_1(solution)
    case_2(solution)
    case_3(solution)


if __name__ == '__main__':
    main()