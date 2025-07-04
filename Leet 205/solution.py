class Solution:
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while 

    preserving the order of characters. No two characters may map to the same character, 
    
    but a character may map to itself.

    Example:

        Input: s = "egg", t = "add"
        Output: true
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        # quick exit
        if len(s) != len(t):
            return False
        
        table: dict[str, str] = dict()
        values: set[str] = set()

        for v1, v2 in zip(s, t):
            if v1 in table:
                if table[v1] != v2:
                    return False
            else:
                # helps with 'no two characters may map to the same character'
                if v2 in values:
                    return False
                
                table[v1] = v2
                values.add(v2)

        return True


def main() -> None:
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))#true
    print(solution.isIsomorphic("foo", "bar"))#false
    print(solution.isIsomorphic("paper", "title"))#true
    print(solution.isIsomorphic("badc", "baba"))#false


if __name__ == "__main__":
    main()