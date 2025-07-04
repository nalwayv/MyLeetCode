class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        # NOTE:
        # since colors represents a circle, 
        # the first and the last tiles are considered to be next to each other.

        n: int = len(colors)
        count: int = 0

        for i in range(n):
            left: int = colors[(i - 1) % n]
            middle: int = colors[i % n]
            right: int = colors[(i + 1) % n]

            if middle != left and middle != right:
                count += 1
        
        return count


def test_case(sol: Solution, colors: list[int], expect: int) -> None:
    print(f"Case: does alternating {colors} equil {expect} ?")
    result: int = sol.numberOfAlternatingGroups(colors)
    print(f"{"":>2}Result: {"pass" if result == expect else "fail"}")


def main() -> None:
    print("3206. Alternating Groups I")

    sol = Solution()
    
    test_case(sol, [0,1,0,0,1], 3)
    test_case(sol, [1,1,1], 0)
    test_case(sol, [0,0,1,0,0], 1)


if __name__ == "__main__":
    main()