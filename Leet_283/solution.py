# Move Zeros
import unittest

class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        """
        !!Do not return anything, modify nums in-place instead!!.

        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        Example 1:

        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Example 2:

        Input: nums = [0]
        Output: [0]

        Constraints:
            - 1 <= nums.length <= 10**4
            - -2**31 <= nums[i] <= 2**31 - 1
        """
        n: int = len(nums)
        if n <= 1:
            return
        
        k: int = 0
        p1: int = 0
        p2: int = 0

        while p1 < n:
            p2 = p1

            # GET ID's THAT ARE NOT ZERO

            while p2 < n - 1 and nums[p2] == 0:
                p2 += 1

            nums[k] = nums[p2]

            k += 1
            p1 = p2 + 1

        # FILL END WITh ZERO'S

        for i in range(k, n):
            nums[i] = 0

    def move_zeroes_2(self, nums: list[int]) -> None:
        """
        """
        # looking for pattern [0, i]
        #   - set [k] to [i]
        #   - set [i] to 0
        #   - int k
        # elif pattern [i, 0]
        #   - skip by setting set k to i
        n: int = len(nums)
        if n <= 1:
            return

        k: int = 0
        for i in range(1, n):
            if nums[i-1] == 0 and nums[i] != 0:
                nums[k] = nums[i]
                nums[i] = 0
                k += 1

            elif nums[i-1] != 0 and nums[i] == 0:
                k = i


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_1(self) -> None:
        nums: list[int] = [0, 1, 0, 3, 12]
        result: list[int] = [1, 3, 12, 0, 0]
        
        self.solution.move_zeroes_2(nums)
        self.assertListEqual(nums, result)

    def test_2(self) -> None:
        nums: list[int] = [0]
        result: list[int] = [0]

        self.solution.move_zeroes_2(nums)
        self.assertListEqual(nums, result)

    def test_3(self) -> None:
        nums: list[int] = [1, 0]
        result: list[int] = [1, 0]

        self.solution.move_zeroes_2(nums)
        self.assertListEqual(nums, result)

    def test_4(self) -> None:
        nums: list[int] = [0, 1]
        result: list[int] = [1, 0]

        self.solution.move_zeroes_2(nums)
        self.assertListEqual(nums, result)

    def test_5(self) -> None:
        nums: list[int] = [1, 0, 1]
        result: list[int] = [1, 1, 0]

        self.solution.move_zeroes_2(nums)
        self.assertListEqual(nums, result)

    def test_6(self) -> None:
        nums: list[int] = [0, 0, 1]
        result: list[int] = [1, 0, 0]

        self.solution.move_zeroes_2(nums)
        self.assertListEqual(nums, result)

    def test_7(self) -> None:
        nums: list[int] = [4,2,4,0,0,3]
        result: list[int] = [4,2,4,3,0,0]

        self.solution.move_zeroes_2(nums)
        self.assertListEqual(nums, result)

    def test_8(self) -> None:
        nums: list[int] = [0,1,0,1,0,1]
        result: list[int] = [1,1,1,0,0,0]

        self.solution.move_zeroes_2(nums)
        self.assertListEqual(nums, result)


def main() -> None:
    solution = Solution()
    # nums: list[int] = [1, 0]
    # nums: list[int] = [0, 1]
    # nums: list[int] = [0,1,0,3,12]
    nums: list[int] = [0,0,1,0,2,3]


    print(f"Input: nums = {nums}")
    solution.move_zeroes(nums)
    print(f"Output: {nums}")


if __name__ == "__main__":
    testing: bool = True

    if testing:
        unittest.main()
    else:
        main()
