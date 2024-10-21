from dataclasses import dataclass


@dataclass
class Word:
    word: str
    count: int


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        """
        words: list[str] = s.split()
        if len(words) != len(pattern):
            return False
        
        # build table
        seen: set[str] = set()
        table: dict[str, Word] = {}
        for i, p in enumerate(pattern):
            if p not in table:
                if words[i] not in seen:
                    table[p] = Word(words[i], 1)
                    seen.add(words[i])
            elif table[p].word == words[i]:
                table[p].count += 1

        # check
        for p in pattern:
            if p in table and table[p].count != 0:
                table[p].count -= 1
            else:
                return False
        return True


def main() -> None:
    print("290. Word Pattern")
    
    sol = Solution()

    case1: bool = sol.wordPattern("abba", "dog cat cat dog")
    print(f"{ "pass" if case1 else "fail" }")

    case2: bool = sol.wordPattern("abba", "dog cat cat fish")
    print(f"{ "pass" if not case2 else "fail" }")

    case3: bool = sol.wordPattern("aaaa", "dog cat cat dog")
    print(f"{ "pass" if not case3 else "fail" }")


if __name__ == "__main__":
    main()