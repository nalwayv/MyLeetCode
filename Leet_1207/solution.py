from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counter: list[tuple[int, int]] = Counter(arr).most_common()
        n: int = len(counter)

        for i in reversed(range(1, n)):
            if counter[i][1] >= counter[i-1][1]:
                return False

        return True


def case1(sol: Solution) -> None:
    arr: list[int] = [1,2,2,1,1,3]
    result: bool = sol.uniqueOccurrences(arr)
    test: str = "pass" if result else "fail"
    print(f"case 1 {test}")


def case2(sol: Solution) -> None:
    arr: list[int] = [1,2]
    result: bool = sol.uniqueOccurrences(arr)
    test: str = "pass" if not result else "fail"
    print(f"case 2 {test}")


def case3(sol: Solution) -> None:
    arr: list[int] = [-3,0,1,-3,1,1,1,-3,10,0]
    result: bool = sol.uniqueOccurrences(arr)
    test: str = "pass" if result else "fail"
    print(f"case 3 {test}")


def main() -> None:
    print("1207. Unique Number of Occurrences")
    
    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()