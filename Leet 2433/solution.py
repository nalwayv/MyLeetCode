class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n: int = len(pref)
        arr = [0] * n
        arr[0] = pref[0]
        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i-1]
        return arr


def main() -> None:
    print('2433. Find The Original Array of Prefix Xor')
    solution = Solution()
    case1 = solution.findArray([5,2,0,3,1])
    print(case1)


if __name__ == '__main__':
    main()