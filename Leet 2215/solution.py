class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        def diff_between(n1: list[int], n2: list[int]) -> list[int]:
            hs: set[int] = set()

            for a in n1:
                hs.add(a)

            for b in n2:
                if b in hs:
                    hs.remove(b)

            return list(hs)

        result: list[list[int]] = []
        
        result.append(diff_between(nums1, nums2))
        result.append(diff_between(nums2, nums1))

        return result


def main() -> None:
    print("2215. Find the Difference of Two Arrays")

    sol = Solution()

    n1: list[int] = [1,2,3]
    n2: list[int] = [2,4,6]

    result: list[list[int]] = sol.findDifference(n1, n2)

    for arr in result:
        print("[", end="")
        for num in arr:
            print(f" {num} ", end="")
        print("]")


if __name__ == "__main__":
    main()