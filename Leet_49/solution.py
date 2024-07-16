class Solution:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        table: dict[str, list[str]] = {}

        for st in strs:
            key = "".join(sorted(st))
            if key in table:
                table[key].append(st)
            else:
                table[key] = list()
                table[key].append(st)

        return list(table.values())

    def print_solution(self, result: list[list[str]]) -> None:
        print("-"*5)
        for i, row in enumerate(result):
            print(f"[{i}]", end=" ")
            for val in row:
                print(f"{val}", end=" ")
            print("")
        print("-"*5)

def main() -> None:

    solution = Solution()

    ## [["bat"],["nat","tan"],["ate","eat","tea"]]
    s1: list[str] = ["eat","tea","tan","ate","nat","bat"]
    r1: list[list[str]] = solution.groupAnagrams(s1)
    solution.print_solution(r1)

    # [[""]]
    s2: list[str] = [""]
    r2: list[list[str]] = solution.groupAnagrams(s2)
    solution.print_solution(r2)

    ## [["a"]]
    s3: list[str] = ["a"]
    r3: list[list[str]] = solution.groupAnagrams(s3)
    solution.print_solution(r3)

    ## [["cab"],["tin"],["pew"],["duh"],["may"],["ill"],["buy"],["bar"][,"max"],["doc"]]
    s4: list[str] = ["cab","tin","pew","duh","hud","may","ill","lli","buy","bar","max","doc"]
    r4: list[list[str]] = solution.groupAnagrams(s4)
    solution.print_solution(r4)


if __name__ == "__main__":
    main()