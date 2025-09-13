class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels: str = 'aeiou'

        count: int = 0
        for ch in s:
            if ch in vowels:
                count += 1

        # p2 win
        if count == 0:
            return False
        
        # p1 win
        if count % 2 != 0:
            return True

        # get max odd vowels
        count: int = 0
        idx: int = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                count += 1
                if count % 2 != 0:
                    idx = i
        
        # try again           
        return self.doesAliceWin(s[idx+1:])


def main() -> None:
    print('3227. Vowels Game in a String')
    solution = Solution()

    print(f'case 1 player 1 should win ? {solution.doesAliceWin('leetcoder')}')
    print(f'case 2 player 1 should not win ? {not solution.doesAliceWin('bbcd')}')
    print(f'case 3 player 1 should win ? {solution.doesAliceWin('a')}')


if __name__ == '__main__':
    main()