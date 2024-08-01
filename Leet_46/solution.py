class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def _get_permutations(i: int, arr: list[int], result: list[list[int]]):
            """ recursively get permutations
            """
            length: int = len(arr)

            if i == length:
                nums: list[int] = [num for num in arr]
                result.append(nums)

            else:
                for j in range(i, length):
                    # swap and then reset
                    arr[i],arr[j] = arr[j],arr[i]
                    _get_permutations(i+1, arr, result)
                    arr[i],arr[j] = arr[j],arr[i]

        result: list[list[int]] = []
        _get_permutations(0, nums, result)

        return result


def main() -> None:
    solution = Solution()
    print(f"{solution.permute([1, 2, 3])}")
    print(f"{solution.permute([0, 1])}")
    print(f"{solution.permute([1])}")


if __name__ == "__main__":
    main()