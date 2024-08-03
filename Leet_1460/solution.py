from collections import defaultdict


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        # need to be of equal length
        # and contain equal amount of dividual ints

        if len(target) != len(arr):
            return False

        table: dict[int, int] = defaultdict(int)
        for a in arr:
            table[a] += 1

        for t in target:
            if t in table and table[t] != 0:
                table[t] -= 1
            else:
                return False

        return True


def main() -> None:
    print("1460. Make Two Arrays Equal by Reversing Subarrays")

    sol = Solution()
    
    print(sol.canBeEqual([1,2,3,4], [2,4,1,3]))
    print(sol.canBeEqual([7], [7]))
    print(sol.canBeEqual([3,7,9], [3,7,11]))


if __name__ == "__main__":
    main()