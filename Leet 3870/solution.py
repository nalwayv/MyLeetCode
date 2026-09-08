class Solution:
    def countCommas(self, n: int) -> int:
        """
        Return the total number of commas used when writing all integers from [1, n] 
        (inclusive) in standard number formatting.

        Constraints:
            n is 1 <= n <= 10**5
        """
        return 0 if n < 1000 else n - 1000 + 1