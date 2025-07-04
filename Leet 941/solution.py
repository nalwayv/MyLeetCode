# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
import unittest


class Solution:
    """
    Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:

    arr.length >= 3

    There exists some i with 0 < i < arr.length - 1 such that:

        arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
    
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    """
    def valid_mountain_array(self, arr: list[int]) -> bool:
        n: int = len(arr)
        
        if not (n >= 3):
            return False

        # find mid going up

        m: int = 0
        for i in range(n - 1):
            if arr[i + 1] > arr[i]:
                m += 1
            else:
                break

        # extream case

        if m == 0 or m == n - 1:
            return False

        # climb down

        for i in range(m , n - 1):
            if arr[i + 1] >= arr[i]:
                return False
            
        return True
    

class Test(unittest.TestCase):
    """
    docs:

    https://docs.python.org/3/library/unittest.html
    
    """
    def setUp(self) -> None:
        self.solution = Solution()

    def test_1_should_return_false(self) -> None:
        arr: list[int] = [2, 1]
        result: bool = self.solution.valid_mountain_array(arr)
        self.assertFalse(result)

    def test_2_should_return_false(self) -> None:
        arr: list[int] = [3, 5, 5]
        result: bool = self.solution.valid_mountain_array(arr)
        self.assertFalse(result)

    def test_3_should_return_true(self) -> None:
        arr: list[int] = [0, 3, 2, 1]
        result: bool = self.solution.valid_mountain_array(arr)
        self.assertTrue(result)

    def test_4_should_return_false(self) -> None:
        arr: list[int] = [9,8,7,6,5,4,3,2,1,0]
        result: bool = self.solution.valid_mountain_array(arr)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
