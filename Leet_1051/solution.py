import unittest

class Solution:
    """
    A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

    You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

    Return the number of indices where heights[i] != expected[i].
    """
    def height_checker(self, heights: list[int]) -> int:
        n: int = len(heights)
        if n <= 1:
            return 1
        
        expected: list[int] = sorted(heights)

        k: int = 0
        for i in range(n):
            if expected[i] != heights[i]:
                k += 1

        return k


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_1(self) -> None:
        heights: list[int] = [1,1,4,2,1,3]
        expected: int = 3
        output: int = self.solution.height_checker(heights)

        self.assertEqual(output, expected)

    def test_2(self) -> None:
        heights: list[int] = [5,1,2,3,4]
        expected: int = 5
        output: int = self.solution.height_checker(heights)

        self.assertEqual(output, expected)

    def test_3(self) -> None:
        heights: list[int] = [1,2,3,4,5]
        expected: int = 0
        output: int = self.solution.height_checker(heights)

        self.assertEqual(output, expected)


def main() -> None:
    solution = Solution()
    heights: list[int] = [1,1,4,2,1,3]

    output: int = solution.height_checker(heights)

    print(f"Input: {heights}")
    print(f"Output: {output}")


if __name__ == "__main__":
    testing: bool = True
    if testing:
        unittest.main()
    else:
        main()