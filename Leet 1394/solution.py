class Solution:
    def findLucky(self, arr: list[int]) -> int:
        table: dict[int, int] = {}

        for num in arr:
            table[num] = table.get(num, 0) + 1
  
        lucky: int = -1
        for key,val in table.items():
            if key == val:
                lucky = max(lucky, key)

        return lucky
    

def main() -> None:
    print("1394. Find Lucky Integer in an Array")

    sol = Solution()
    print(sol.findLucky([2,2,3,4]))


if __name__ == "__main__":
    main()