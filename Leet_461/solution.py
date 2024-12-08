class Solution:
    def get_hamming_distance(self, str1: str, str2: str) -> int:
        """Calculate hamming distance
        """
        # count times that s1[i] != s2[i]
        # get_hamming_distance(1, 4)
        #    1: 0 0 0 1
        #    4: 0 1 0 0
        #    2:   x   x

        n: int = len(str1)
        m: int = len(str2)

        if n != m:
            return -1
        
        dis: int = 0
        for i in range(n):
            if str1[i] != str2[i]:
                dis += 1

        return dis

    def hammingDistance(self, x: int, y: int) -> int:
        return self.get_hamming_distance("{:032b}".format(x), "{:032b}".format(y))


def main() -> None:
    print("461. Hamming Distance")

    sol = Solution()
    
    print(sol.hammingDistance(1, 4) == 2)
    print(sol.hammingDistance(3, 1) == 1)


if __name__ == "__main__":
    main()