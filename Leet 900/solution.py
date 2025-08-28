class RLEIterator:
    """
    RLEIterator provides an iterator over a run-length encoded sequence.
    Attributes:
        idx (int): Current index in the run-length encoding.
        amount (list[int]): List of counts for each value.
        nums (list[int]): List of values corresponding to counts.
        length (int): Number of unique values in the encoding.
    Methods:
        __init__(encoding: list[int]):
            Initializes the iterator with a run-length encoded list.
            The encoding is a list where even indices represent counts and odd indices represent values.
        next(n: int) -> int:
            Consumes 'n' elements from the iterator and returns the last value exhausted.
            Returns -1 if there are not enough elements left.
    """
    def __init__(self, encoding: list[int]):
        self.idx: int = 0
        self.amount: list[int] = []
        self.nums: list[int] = []

        for i in range(0, len(encoding), 2):
            if encoding[i] > 0:
                self.amount.append(encoding[i])
                self.nums.append(encoding[i+1])

        self.length: int = len(self.nums)

    def next(self, n: int) -> int:
        """
        Returns the element being processed after consuming 'n' elements from the run-length encoded sequence.
        Args:
            n (int): The number of elements to consume from the sequence.
        Returns:
            int: The value of the element being processed after consuming 'n' elements,
                 or -1 if there are not enough elements left in the sequence.
        """
        while self.idx < len(self.nums):
            if self.amount[self.idx] >= n:
                self.amount[self.idx] -= n
                return self.nums[self.idx]
            
            n -= self.amount[self.idx]
            self.idx += 1

        return -1


def case_1() -> None:
    print("Case 1")
    data = [3,8,0,9,2,5]
    rle = RLEIterator(data)
    for n,expect in zip(
        [2,1,1,2],
        [8,8,5,-1]):
        print(f"{rle.next(n)} == {expect}")


def case_2() -> None:
    print("Case 2")
    data = [784,303,477,583,909,505]
    rle = RLEIterator(data)
    for n, expect in zip(
        [130,333,238,87,301,276],
        [303,303,303,583,583,505]):
        print(f"{rle.next(n)} == {expect}")


def main() -> None:
    print("900. RLE Iterator")
    case_1()
    case_2()


if __name__ == "__main__":
    main()