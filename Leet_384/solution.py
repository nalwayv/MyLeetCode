import random

class Solution:
    def __init__(self, nums: list[int]):
        self._nums: list[int] = nums
        self._restore: list[int] = [n for n in nums]

    def reset(self) -> list[int]:
        for i, num in enumerate(self._restore):
            self._nums[i] = num
        return self._nums

    def shuffle(self) -> list[int]:
        random.shuffle(self._nums)
        return self._nums


def main() -> None:
    print("384. Shuffle an Array")

    sol = Solution([1,2,3])
    shuffel = sol.shuffle()
    print(shuffel)

    shuffel = sol.shuffle()
    print(shuffel)

    reset = sol.reset()
    print(reset)


if __name__ == "__main__":
    main()