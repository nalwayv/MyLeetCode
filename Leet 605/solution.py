class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length: int = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                # edge case else check left and right
                if (i == 0 and i+1 < length and flowerbed[i+1] == 0) or (i == length-1 and flowerbed[i-1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
        return n <= 0
    

def main() -> None:
    print("605. Can Place Flowers")
    
    sol = Solution()
    print(sol.canPlaceFlowers([1,0,0,0,1], 1) == True)
    print(sol.canPlaceFlowers([1,0,0,0,1], 2) == False)
    print(sol.canPlaceFlowers([0,0,1,0,1], 1) == True)
    print(sol.canPlaceFlowers([0], 1) == True)


if __name__ == "__main__":
    main()