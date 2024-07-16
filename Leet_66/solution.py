    
class Solution:
    """
    You are given a large integer represented as an integer array digits, 
    
    where each digits[i] is the ith digit of the integer. 
    
    The digits are ordered from most significant to least significant in left-to-right order. 
    
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
    
    Example:

        Input: digits = [1,2,3]

        Output: [1,2,4]

        Explanation: The array represents the integer 123.

        Incrementing by one gives 123 + 1 = 124.

        Thus, the result should be [1,2,4].
    """
    def concat_ints(self, digits: list[int])-> int:
        result: int = 0
        for num in digits:
            result *= 10
            result += num
        return result

    def count_digits(self, digit: int) -> int:
        count: int = 0
        while True:
            digit//=10
            count += 1
            if digit == 0:
                break
        return count

    def deconstruct_int(self, digit: int) -> list[int]:
        count: int = self.count_digits(digit)
        result: list[int] = [0] * count

        at: int = count
        while at != 0:
            current: int = digit % 10
            digit //= 10
            result[at-1] = current
            at -= 1
        return result

    def plusOne(self, digits: list[int]) -> list[int]:
        return self.deconstruct_int(self.concat_ints(digits) + 1)


        
def main() -> None:
    solution = Solution()
    digits: list[int] = []
    result: list[int] = solution.plusOne(digits)
    print(f"Output: {result}")



if __name__ == "__main__":
    main()