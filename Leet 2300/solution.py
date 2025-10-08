class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Given two lists, `spells` and `potions`, and an integer `success`, this function computes for each spell the number of potions that can be paired with it such that the product of the spell and potion is greater than or equal to `success`.
        Args:
            spells (list[int]): A list of integers representing the strength of each spell.
            potions (list[int]): A list of integers representing the strength of each potion.
            success (int): The minimum required product for a successful pair.
        Returns:
            list[int]: A list where the ith element is the number of potions that can be paired with the ith spell to achieve at least the `success` threshold.
        """
        potions.sort()
        potions_length: int = len(potions)

        for i, s in enumerate(spells):
            if s * potions[-1] < success:
                spells[i] = 0
            else:
                lo: int = 0
                hi: int = potions_length 
                while lo < hi:
                    mid: int = (hi+lo) // 2

                    if s * potions[mid] >= success:
                        hi = mid
                    else:
                        lo = mid + 1
                spells[i] = potions_length - lo

        return spells


def main() -> None:
    print('2300. Successful Pairs of Spells and Potions')

    solution = Solution()

    case1: list[int] = solution.successfulPairs([5,1,3], [1,2,3,4,5], 7)
    print(f'case 1 should equal [4,0,3]? {case1}')


    case2: list[int] = solution.successfulPairs([3,1,2], [8,5,8], 16)
    print(f'case 2 should equal [2,0,2]? {case2}')


if __name__ == '__main__':
    main()

