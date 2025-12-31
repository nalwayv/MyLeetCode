class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        nums.sort()
        n: int = len(nums)
        seen: set[tuple[int, int, int]] = set()
        
        for i in range(n - 2):
            target: int = -nums[i]
            left: int = i + 1
            right: int = n - 1
            
            while left < right:
                total: int = nums[left] + nums[right]
                if total == target:
                    current_sum = (nums[i], nums[left], nums[right])
                    if current_sum not in seen:
                        seen.add(current_sum)
                        result.append(list(current_sum))
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return result


def main() -> None:
    print('15. 3Sum')

    solution = Solution()
    
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0,0,0]))
    print(solution.threeSum([-2,0,1,1,2]))


if __name__ == '__main__':
    main()