import unittest

class Solution:
    """
    Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

    Example 1:

    Input: arr = [10,2,5,3]
    Output: true
    Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

    Example 2:

    Input: arr = [3,1,7,11]
    Output: false
    Explanation: There is no i and j that satisfy the conditions.
    """
    def check_if_exist(self, arr: list[int]) -> bool:
        n: int = len(arr)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if arr[i] == (2 * arr[j]) or arr[j] == (2 * arr[i]):
                    return True

        return False
        

class Test(unittest.TestCase):
    """
    docs:

    https://docs.python.org/3/library/unittest.html
    
    run:

    []$ python -m unittest -v test_leet_1346.py
    """
    def setUp(self) -> None:
        self.solution = Solution()

    def test_case_1_should_equil_true(self) -> None:
        arr: list[int] = [10, 2, 5, 3]
        result: bool = self.solution.check_if_exist(arr)
        self.assertTrue(result)

    def test_case_2_should_equil_false(self) -> None:
        arr: list[int] = [3, 1, 7, 11]
        result: bool = self.solution.check_if_exist(arr)
        self.assertFalse(result)

    def test_case_3_should_equil_true(self) -> None:
        arr: list[int] = [7, 1, 14, 11]
        result: bool = self.solution.check_if_exist(arr)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()