class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Returns the 'Majority' element from nums

        len(nums) has to be at least 1

        Example:
        >>> majorityElement([3,2,3])
        3
        """
        # if not nums:
        #     raise Exception("len(nums) cant be zero")
        
        n: int = len(nums)
        if n == 1:
            return nums[0]
        
        counter: dict[int, int] = {}
        majority: int = n // 2
        
        max_count: int = 0
        max_number: int = 0
        
        # count numbers and check if counter[num] meets the conditions to be the majority result
        for num in nums:
            if num in counter:
                counter[num] += 1

                if counter[num] > majority and counter[num] > max_count:
                    max_count = counter[num]
                    max_number = num
            else:
                counter[num] = 1

        return max_number


def main() -> None:
    print("169. Majority Element")
    
    sol = Solution()

    nums: list[int] = [3,2,3]
    result: int = sol.majorityElement(nums)
    print(f"case 1 { "pass" if result == 3 else "fail" }")


if __name__ == "__main__":
    main()