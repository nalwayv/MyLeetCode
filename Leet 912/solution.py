class Solution:
    # merge sort
    def _merge(self, nums: list[int], tmp: list[int],lo: int, mid:int, hi: int) -> None:
        lo_start: int = lo
        lo_stop: int = mid
        hi_start: int = mid+1
        hi_stop: int = hi
        idx: int = lo

        while lo_start <= lo_stop and hi_start <= hi_stop:
            if nums[lo_start] < nums[hi_start]:
                tmp[idx] = nums[lo_start]
                idx += 1
                lo_start += 1
            else:
                tmp[idx] = nums[hi_start]
                idx += 1
                hi_start += 1

        while lo_start <= lo_stop:
            tmp[idx] = nums[lo_start]
            idx += 1
            lo_start += 1

        while hi_start <= hi_stop:
            tmp[idx] = nums[hi_start]
            idx += 1
            hi_start += 1

        for idx in range(lo, hi + 1):
            nums[idx] = tmp[idx]

    def _sort(self, nums: list[int], tmp: list[int], lo: int, hi: int) -> None:
        if lo >= hi:
            return
        
        mid: int = (lo + hi) // 2

        self._sort(nums, tmp, lo, mid)
        self._sort(nums, tmp, mid+1, hi)
        self._merge(nums, tmp, lo, mid, hi)

    def sortArray(self, nums: list[int]) -> None:
        n: int = len(nums)
        tmp: list[int] = [0]*n
        self._sort(nums, tmp, 0, n-1)


def main() -> None:
    print("912. Sort an Array")
    sol = Solution()
    case1: list[int] = [5,2,3,1]
    sol.sortArray(case1)
    print(case1)

    case2: list[int] = [5,1,1,2,0,0]
    sol.sortArray(case2)
    print(case2)


if __name__ == "__main__":
    main()