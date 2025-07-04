class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m: int = len(word1)
        n: int = len(word2)

        res: list[str] = []

        j: int = 0

        # if word1 length is more then word2 length
        # use two pointer with j being slow
        
        if m > n:
            for i in range(m):
                res.append(word1[i])
                if j < n:
                    res.append(word2[j])
                    j += 1
        else:
            for i in range(n):
                if j < m:
                    res.append(word1[j])
                    j += 1
                res.append(word2[i])

        # python build string

        return "".join(res)   