# class Iterator:
#     def __init__(self, nums: list[int]) -> None:
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#     def hasNext(self) -> bool:
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#     def next(self) -> int:
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator: Iterator) -> None:
        tmp: list[int] = []
        while iterator.hasNext():
            tmp.append(iterator.next())

        self.stk: list[int] = []
        while tmp:
            self.stk.append(tmp.pop())

    def peek(self) -> int:
        if self.stk:
            return self.stk[-1]
        return -1

    def next(self) -> int:
        if self.stk:
            return self.stk.pop()
        return -1

    def hasNext(self) -> bool:
        return len(self.stk) != 0


def main() -> None:
    print("284. Peeking Iterator")

    itr = PeekingIterator(Iterator([1,2,3]))
    print("next: ", itr.next())
    print("peek: ", itr.peek())
    print("next: ", itr.next())
    print("next: ", itr.next())
    print("has next: ", itr.hasNext())


if __name__ == "__main__":
    main()
