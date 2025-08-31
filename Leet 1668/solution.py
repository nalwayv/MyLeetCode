class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        Finds the maximum number of times the substring 'word' repeats consecutively in the string 'sequence'.
        Args:
            sequence (str): The string in which to search for repeated occurrences of 'word'.
            word (str): The substring to search for consecutive repetitions.
        Returns:
            int: The maximum number of consecutive repetitions of 'word' found in 'sequence'.
        """
        count: int = 0
        i: int = 1
        while True:
            if word * i in sequence:
                count += 1
            else:
                break
            i += 1
        return count


def main() -> None:
    print('1668. Maximum Repeating Substring')

    solution = Solution()

    case_1: int = solution.maxRepeating(sequence='ababc', word='ab')
    print(f'case 1 should equal 2 ? {case_1}')

    case_2: int = solution.maxRepeating(sequence='ababc', word='ba')
    print(f'case 2 should equal 1 ? {case_2}')

    case_3: int = solution.maxRepeating(sequence='ababc', word='ac')
    print(f'case 3 should equal 0 ? {case_3}')
    
    case_4: int = solution.maxRepeating(sequence='aaabaaaabaaabaaaabaaaabaaaabaaaaba', word='aaaba')
    print(f'case 4 should equal 5 ? {case_4}')

    case_5: int = solution.maxRepeating(sequence='a', word='a')
    print(f'case 5 should equal 1 ? {case_5}')


if __name__ == '__main__':
    main()
