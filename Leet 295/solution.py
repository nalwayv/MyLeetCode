import heapq

class MedianFinder:
    def __init__(self) -> None:
       self._lo: list[int] = []
       self._hi: list[int] = []
       self._median: float = 0

    def addNum(self, num: int) -> None:
        if len(self._lo) == len(self._hi):
            heapq.heappush_max(self._lo, heapq.heappushpop(self._hi, num))
            self._median = self._lo[0]
        else:
            heapq.heappush(self._hi, heapq.heappushpop_max(self._lo, num))
            self._median = (self._lo[0] + self._hi[0]) / 2

    def findMedian(self) -> float:
        return self._median
    

def main() -> None:
    print("295. Find Median from Data Stream")


if __name__ == "__main__":
    main()