from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        table: dict[int, list[int]] = defaultdict(list)
        for idx, val in enumerate(groupSizes):
            table[val].append(idx)

        result: list[list[int]] = []
        for size, indices in table.items():
            for j in range(0, len(indices), size):
                result.append(indices[j:j+size])

        return result


def main() -> None:
    print("1282. Group the People Given the Group Size They Belong To")

    sol = Solution()
    
    print(sol.groupThePeople([3,3,3,3,3,1,3]))
    print(sol.groupThePeople([2,1,3,3,3,2]))


if __name__ == "__main__":
    main()