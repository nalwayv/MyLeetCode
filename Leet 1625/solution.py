from collections import deque

class Solution:
    def _rotate(self, s: str, k: int) -> str:
        n: int = len(s)
        r: str = ''
        p: int = abs(n - k) % n
        for _ in range(n):
            r += s[p]
            p = (p + 1) % n
        return r

    def _odd(self, s: str, k: int) -> str:
        r: str = ''
        for i, v in enumerate(s):
            if i%2 != 0:
                num: int = int(v)
                num = (num + k) % 10
                r += str(num)
            else:
                r += v
        return r

    def _bfs(self, s: str, a: int, b: int) -> str:
        que: deque[str] = deque([s])
        visited: set[str] = {s}
        smallest: str = s

        while que:
            curr_s: str = que.popleft()
            smallest = min(smallest, curr_s)

            odd_s: str = self._odd(curr_s, a)
            rotate_s: str = self._rotate(curr_s, b)

            if odd_s not in visited:
                visited.add(odd_s)
                que.append(odd_s)

            if rotate_s not in visited:
                visited.add(rotate_s)
                que.append(rotate_s)

        return smallest

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        return self._bfs(s, a, b)


def main() -> None:
    print('1625. Lexicographically Smallest String After Applying Operations')
    
    sol = Solution()

    print(sol.findLexSmallestString('5525', 9, 2))
    print(sol.findLexSmallestString('74', 5, 1))
    print(sol.findLexSmallestString('0011', 4, 2))


if __name__ == '__main__':
    main()