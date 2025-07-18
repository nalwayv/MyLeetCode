class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        """
        Constructs a sequence of "Push" and "Pop" operations to build the given target array using a stack.
        
        Args:
            target (list[int]): The target array to build using stack operations.
            n (int): The maximum number to read from (numbers are read from 1 to n).
        
        Returns:
            list[str]: A list of operations ("Push" and "Pop") that will build the target array.
        """
        result: list[str] = []
        top: int = 0

        for num in range(1, n + 1):
            if top == len(target):
                break

            result.append("Push")
            if num != target[top]:
                result.append("Pop")
            else:
                top += 1

        return result


def main() -> None:
    print("1441. Build an Array With Stack Operations")
    sol = Solution()

    print(sol.buildArray(target=[1,3], n=3))
    print(sol.buildArray(target=[1,2,3], n=3))


if __name__ == "__main__":
    main()