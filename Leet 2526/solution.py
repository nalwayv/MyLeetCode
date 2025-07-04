class DataStream:
    def __init__(self, value: int, k: int):
        self.value: int = value
        self.k: int = k
        self.count: int = 0

    def consec(self, num: int) -> bool:
        # -- reset
        if num != self.value:
            self.count = 0
            return False
        
        # -- is already at max
        if self.count == self.k:
            return True
        
        self.count += 1
        return self.count == self.k


def main() -> None:
    print("2526. Find Consecutive Integers from a Data Stream")
    ds = DataStream(4,3)

    print(f"consec(4) = False ? {'pass' if not ds.consec(4) else 'fail'}")
    print(f"consec(4) = False ? {'pass' if not ds.consec(4) else 'fail'}")
    print(f"consec(4) = True ? {'pass' if ds.consec(4) else 'fail'}")
    print(f"consec(3) = False ? {'pass' if not ds.consec(3) else 'fail'}")


if __name__ == "__main__":
    main()