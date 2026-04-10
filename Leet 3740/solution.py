class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        table: dict[int, list[int]] = {}
        for idx, val in enumerate(nums):
            if val not in table:
                table[val] = []
            table[val].append(idx)

        min_dist: float = float('inf')
        for val in table.values():
            if len(val) < 3:
                continue
            
            for i in range(len(val) - 3 + 1):
                window = val[i:i+3]
                ij: int = abs(window[0] - window[1])
                jk: int = abs(window[1] - window[2])
                ki: int = abs(window[2] - window[0])
                min_dist = min(min_dist, ij + jk + ki)

        return -1 if min_dist == float('inf') else int(min_dist)
    
print('3740. Minimum Distance Between Three Equal Elements I')
solution = Solution()
print(solution.minimumDistance([1,2,1,1,3]))
print(solution.minimumDistance([1,1,2,3,2,1,2]))
print(solution.minimumDistance([1]))