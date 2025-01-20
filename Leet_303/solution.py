class NumArray:
    def __init__(self, nums: list[int]) -> None:
        # prefix sum
        n: int = len(nums)
        self._nums = [0] * n
        self._nums[0] = nums[0]
        for i in range(1, n):
            self._nums[i] = self._nums[i - 1] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        return self._nums[right] if left == 0 else self._nums[right] - self._nums[left - 1]


def main() -> None:
    print("303. Range Sum Query - Immutable")

    nums: list[int] = [-2, 0, 3, -5, 2, -1]
    
    numArr = NumArray(nums)
    
    print(f"Nums: {nums}")
    print(f"SumRange(0, 2) {numArr.sumRange(0, 2)} == 1")
    print(f"SumRange(2, 5) {numArr.sumRange(2, 5)} == -1")
    print(f"SumRange(0, 5) {numArr.sumRange(0, 5)} == -3")


if __name__ == "__main__":
    main()
