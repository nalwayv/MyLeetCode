class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n: int = len(boxes)
        result: list[int] = [0 for _ in range(n)]
        
        # store idx of boxes that have a value of 1
        idxs: list[int] = [i for i in range(n) if boxes[i] == "1"]

        for i in range(n):
            for j in idxs:
                result[i] += abs(i-j)
        
        return result


def main() -> None:
    print("1769. Minimum Number of Operations to Move All Balls to Each Box")
    
    sol = Solution()

    print(sol.minOperations("110"))
    print(sol.minOperations("001011"))


if __name__ == "__main__":
    main()
