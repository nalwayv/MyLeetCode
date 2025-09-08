class Solution:
    def get_no_zero_integers(self, n: int) -> list[int]:
        """
        Finds two positive integers whose sum is equal to the given integer `n`, 
        and neither integer contains the digit '0' in its decimal representation.
        Args:
            n (int): The target sum for the two integers.
        Returns:
            list[int]: A list containing the two integers that sum to `n` and do not contain the digit '0'.
        """
        no_zero_ints: list[int] =  [i for i in range(n) if '0' not in str(i)]

        start: int = 0
        end: int = len(no_zero_ints) - 1

        while start < end:
            val: int = no_zero_ints[start] + no_zero_ints[end]
            
            if val == n:
                break

            if val < n:
                start += 1
            else:
                end -= 1

        return [no_zero_ints[start], no_zero_ints[end]]


def main() -> None:
    print('1317. Convert Integer to the Sum of Two No-Zero Integers')

    solution = Solution()
    
    print(solution.get_no_zero_integers(n=2))
    print(solution.get_no_zero_integers(n=11))


if __name__ == '__main__':
    main()