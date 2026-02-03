class Solution:
    def inc(self, nums: list[int], start: int):
        p1: int = start
        for i in range(start + 1, len(nums)):
            if nums[i - 1] < nums[i]:
                p1 += 1
            else:
                break
        return p1

    def dec(self, nums: list[int], start: int):
        p1: int = start
        for i in range(start + 1, len(nums)):
            if nums[i-1] > nums[i]:
                p1 += 1
            else: 
                break
        return p1

    def isTrionic(self, nums: list[int]) -> bool:
        going_up: bool = True
        up: int = 0
        down: int = 0
        p1: int = 0

        while p1 < len(nums) - 1:
            if going_up:
                # peak
                p2: int = p1
                p1 = self.inc(nums, p1)
                
                # no change in elevation
                if p1 == p2:
                    return False
                
                up += 1
                going_up = False
            else:
                # vally
                p2: int = p1
                p1 = self.dec(nums, p1)

                # no change in elevation
                if p1 == p2:
                    return False
                
                down += 1
                going_up = True

        return up + down == 3


def main() -> None:
    print('3637. Trionic Array I')

    solution = Solution()
    
    test_cases = [
        ([1, 3, 5, 4, 2, 6], True),
        ([2, 1, 3], False),
        ([6, 7, 5, 1], False),
        ([1, 2, 3], False),
        ([8, 9, 4, 6, 1], False),
    ]
    
    for nums, expected in test_cases:
        result: bool = solution.isTrionic(nums)
        status: str = 'pass' if result == expected else 'fail'
        print(f'{status} {nums} -> {result}')


if __name__ == '__main__':
    main()