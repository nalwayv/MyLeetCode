class Solution:
    """
    Write an algorithm to determine if a number n is happy.
    """
    # Note(nike): I never herd of a happy number before
    # happy number: https://en.wikipedia.org/wiki/Happy_number
    # perfect digit: https://en.wikipedia.org/wiki/Perfect_digital_invariant

    # Note(nick) my first method was to just deconstruct the int and squ sum
    # its ints
    
    # def deconstruct(self, n: int) -> list[int]:
    #     base: int = 10
    #     result: list[int] = []
    #     while n > 0:
    #         result.append(n % base)
    #         n //= base
    #     return result
    
    # def squ_sum(self, nums: list[int]) -> int:
    #     total: int = 0
    #     for n in nums:
    #         total += (n * n)
    #     return total

    def perfect_digit_invariant(self, num: int) -> int:
        base: int = 10
        total: int = 0
        while num > 0:
            total += (num % base) * (num % base)
            num //= base
        return total
    
    def isHappy(self, n: int) -> bool:
        hash_set: set[int] = set()
        while n > 1 and n not in hash_set:
            hash_set.add(n)
            n = self.perfect_digit_invariant(n)
            print(n)
        return n == 1


def main() -> None:
    solution = Solution()
    # print(solution.isHappy(13))
    # print(solution.isHappy(19))
    # print(solution.isHappy(4))
    print(solution.isHappy(2147483647))


if __name__ == "__main__":
    main()