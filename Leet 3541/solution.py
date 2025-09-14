class Solution:
    def maxFreqSum(self, s: str) -> int:
        """
        Calculates the sum of the highest frequency of any vowel and the highest frequency of any consonant in the input string.
        Args:
            s (str): The input string to analyze.
        Returns:
            int: The sum of the maximum frequency of any vowel and the maximum frequency of any consonant in the string.
        """
        fr: dict[str, int] = {}
        vowels: str = 'aeiou'

        max_vowels: int = 0
        max_conconants: int = 0

        for ch in s:
            if ch in vowels:
                fr[ch] = fr.get(ch, 0) + 1
                max_vowels = max(max_vowels, fr[ch])
            else:
                fr[ch] = fr.get(ch, 0) + 1
                max_conconants = max(max_conconants, fr[ch])

        return max_vowels + max_conconants
    

def main() -> None:
    print('3541. Find Most Frequent Vowel and Consonant')
    
    solution = Solution()

    print(f'case 1 {solution.maxFreqSum(s='successes')}')
    print(f'case 2 {solution.maxFreqSum(s='aeiaeia')}')


if __name__ == '__main__':
    main()