class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        p1: int = 0
        p2: int = len(piles) - 2
        result: int = 0
        while p1 < p2:
            result += piles[p2]
            p1 += 1
            p2 -= 2
        return result
    

def main() -> None:
    print('1561. Maximum Number of Coins You Can Get')

    solution= Solution()
    pile1 = [2,4,1,2,7,8]
    case1 = solution.maxCoins(pile1)
    print(f'max coins for [2,4,1,2,7,8] should equal 9? {'pass' if case1 == 9 else 'fail'}')


if __name__ == '__main__':
    main()