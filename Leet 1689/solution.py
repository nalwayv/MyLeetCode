class Solution:
    def minPartitions(self, n: str) -> int:
        # Just get max digit from digits
        result: int = -1
        for num in n:
            result = max(result, int(num))
        return result
    

def main() -> None:
    print("1689. Partitioning Into Minimum Number Of Deci-Binary Numbers")
    
    sol = Solution()

    case_1 = sol.minPartitions("32")
    print(f"{case_1} = 3")
    
    case_2 = sol.minPartitions("82734")
    print(f"{case_2} = 8")

    case_3 = sol.minPartitions("27346209830709182346")
    print(f"{case_3} = 9")

    case_4 = sol.minPartitions("3")
    print(f"{case_4} = 3")


if __name__ == "__main__":
    main()