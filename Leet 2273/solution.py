class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        table: dict[str, str] = {
            w: ''.join(sorted(w))
            for w in words
        }

        result: list[str] = []
        prev: str = ''
        for w in words:
            curr: str = table[w]
            if prev != curr:
                prev = curr
                result.append(w)

        return result


def main() -> None:
    print('2273. Find Resultant Array After Removing Anagrams')
    
    solution = Solution()

    print(solution.removeAnagrams(['abba', 'baba', 'bbaa', 'cd', 'cd']))
    print(solution.removeAnagrams(['a', 'b', 'a']))


if __name__ == '__main__':
    main()