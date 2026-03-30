from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        even = Counter([v for i,v in enumerate(s1) if i%2==0]) == Counter([v for i,v in enumerate(s2) if i%2==0])
        if not even:
            return False
        return Counter([v for i,v in enumerate(s1) if i%2!=0]) == Counter([v for i,v in enumerate(s2) if i%2!=0])


def main() -> None:
    print('2840. Check if Strings Can be Made Equal With Operations II')
    
    case1: bool = Solution().checkStrings('abcdba', 'cabdab')
    case1_result: str = 'pass' if case1 else 'fail'
    print(f'case1 should pass? {case1_result}')


if __name__ == '__main__':
    main()