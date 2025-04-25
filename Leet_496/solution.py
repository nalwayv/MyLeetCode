class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # table of nums and their next greatest value
        nxt: dict[int, int] = {}
        stk: list[int] = []

        for val in nums2:
            # keep popping stack while its top is less val
            while stk and stk[-1] < val:
                nxt[stk.pop()] = val
            stk.append(val)

        # if num is in nxt then add to result else -1
        result: list[int] = []
        for num in nums1:
            if num in nxt:
                result.append(nxt[num])
            else:
                result.append(-1)

        return result


def main() -> None:
    print("496. Next Greater Element I")
    sol = Solution()
    print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))
    print(sol.nextGreaterElement([2,4], [1,2,3,4]))
    print(sol.nextGreaterElement([1], [1,2,3,4]))


if __name__ == "__main__":
    main()