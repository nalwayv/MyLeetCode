class Solution:
    def smallestNumber(self, num: int) -> int:
        """Given an integer num. 
        Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.
        """

        # get sign

        sign: int = -1 if num < 0 else 1
        if sign < 0:
            num *= -1

        # break down number

        nums: list[int] = []
        if num == 0:
            nums.append(0)
        else:
            while num > 0:
                nums.append(num % 10)
                num //= 10
        
        # build result

        result: int = 0
        if sign < 0:
            nums.sort(reverse=True)
            
            for num in nums:
                result *= 10
                result += num
        else:
        
            nums.sort()

            # swap first non zero value
            n: int = len(nums)
            i: int = 0
            for _ in range(1, n):
                if nums[i] != 0:
                    break
                i += 1
            nums[0], nums[i] = nums[i], nums[0]

            result: int = 0
            for num in nums:
                result *= 10
                result += num
    
        return result * sign


def main() -> None:
    print("2165. Smallest Value of the Rearranged Number")

    sol = Solution()

    print("case 1")
    print(sol.smallestNumber(num= 310))

    print("case 2")
    print(sol.smallestNumber(num= -7605))

    print("case 3")
    print(sol.smallestNumber(num= 0))


if __name__ == "__main__":
    main()