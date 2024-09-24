class TNode:
    def __init__(self) -> None:
        # only storing number stings 0-9 
        self.children: list[TNode|None] = [None] * 10
        self.end: bool = False

class Trie:
    def __init__(self) -> None:
        self.root: TNode|None = TNode()

    def put(self, key: str) -> None:
        current: TNode|None = self.root
        
        for c in key:
            if current:
                # clamp ord number between 0 and 9
                idx: int = ord(c) - ord('0')

                if current.children[idx] == None:
                    current.children[idx] = TNode()

                current = current.children[idx]
        if current:
            current.end = True

    def _longest_prefix(self, root: TNode|None, query: str, length: int, depth: int) -> int:
        """ recursive check tree for longest common prefix
        """
        if root == None:
            return length

        length = depth
        
        if depth == len(query):
            return length
        
        # clamp ord number between 0 and 9
        idx: int = ord(query[depth]) - ord('0')

        return self._longest_prefix(root.children[idx], query, length, depth+1)

    def longest_prefix(self, query: str) -> int:
        return self._longest_prefix(self.root, query, 0, 0)


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        tri = Trie()

        for val in arr1:
            tri.put(str(val))

        result: int = 0
        for b in arr2:
            lp: int = tri.longest_prefix(str(b))
            result = max(result, lp)

        return result
    
    def brute_force(self, arr1: list[int], arr2: list[int]) -> int:
        result: int = 0
        for a in arr1:
            s1: str = str(a)

            for b in arr2:
                s2: str = str(b)

                if s1[0] == s2[0]:

                    n1: int = len(s1)
                    n2: int = len(s2)

                    n: int = n1 if n1 < n2 else n2
                    while n != 0 and s1[:n] != s2[:n]:
                        n -= 1

                    result = max(result, n)
                    
        return result


def main() -> None:
    print("3043. Find the Length of the Longest Common Prefix")

    sol = Solution()

    case_1: int = sol.longestCommonPrefix([1,10,100],[1000])
    print(f"case_1 {"pass" if case_1 == 3 else "fail"}")

    case_2: int = sol.longestCommonPrefix([1,2,3],[4,4,4])
    print(f"case_2 {"pass" if case_2 == 0 else "fail"}")



if __name__ == "__main__":
    main()

