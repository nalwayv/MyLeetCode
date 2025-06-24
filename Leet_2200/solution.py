class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        nums_length: int = len(nums)
        keys: list[int] = [i for i in range(nums_length) if nums[i] == key]
        keys_length: int = len(keys)
        result: list[int] = []

        j: int = 0
        for i in range(nums_length):
        
            while j < keys_length and keys[j] < i - k:
                j += 1

            if k < keys_length and abs(keys[j] - i) <= k:
                result.append(i)
        
        return result


def main() -> None:
    print("2200. Find All K-Distant Indices in an Array")
    
    sol = Solution()

    print(sol.findKDistantIndices([3,4,9,1,3,9,5], 9, 1)) # [1,2,3,4,5,6]
    print(sol.findKDistantIndices([2,2,2,2,2], 2, 2)) # [0,1,2,3,4]


if __name__ == "__main__":
    main()