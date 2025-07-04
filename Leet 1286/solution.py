from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = ["".join(c) for c in combinations(characters, combinationLength)]

    def next(self) -> str:
        return self.combinations.pop(0)

    def hasNext(self) -> bool:
        return len(self.combinations) != 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


def main() -> None:
    print("__ 1286. Iterator for Combination __")

    combination = CombinationIterator("abc", 2)
    while combination.hasNext():
        print(combination.next())


if __name__ == "__main__":
    main()