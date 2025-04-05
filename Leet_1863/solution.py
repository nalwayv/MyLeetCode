class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        n: int = len(nums)
        sum_total: int = 0

        for i in range(pow(2, n)):
            current_xor_sum: int = 0

            for j, b in enumerate(bin(i)[2:].zfill(n)):
                if b == "1":
                    current_xor_sum ^= nums[j]
            
            sum_total += current_xor_sum

        return sum_total


def main() -> None:
    print("1863. Sum of All Subset XOR Totals")

    sol = Solution()
    
    print(f"Result ([1,3]) = {sol.subsetXORSum([1,3])}")
    print(f"Result ([5,1,6]) = {sol.subsetXORSum([5,1,6])}")


if __name__ == "__main__":
    main()