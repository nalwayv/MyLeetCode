from collections import Counter


class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]) -> None:
        self.nums1 = nums1
        self.nums2 = nums2
        self.table: Counter[int] = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        if index >= 0 and index < len(self.nums2):
            # subtract frequency
            self.table[self.nums2[index]] -= 1
            
            # update
            self.nums2[index] += val
            self.table[self.nums2[index]] = self.table.get(self.nums2[index], 0) + 1

    def count(self, tot: int) -> int:
        count: int = 0
        for num in self.nums1:
            count += self.table.get(tot - num, 0)
        return count


def main() -> None:
    print("1865. Finding Pairs With a Certain Sum")

    findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
    print(findSumPairs.count(7))        # return 8
    findSumPairs.add(3, 2)              # now nums2 = [1,4,5,4,5,4]
    print(findSumPairs.count(8))        # return 2
    print(findSumPairs.count(4))        # return 1
    findSumPairs.add(0, 1)              # now nums2 = [2,4,5,4,5,4]
    findSumPairs.add(1, 1)              # now nums2 = [2,5,5,4,5,4]
    print(findSumPairs.count(7))        # return 11


if __name__ == "__main__":
    main()
