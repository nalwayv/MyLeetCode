def maximumLength(nums: list[int]) -> int:
    freq: dict[int, int] = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    result: int = freq.get(1, 0)
    if result > 0:
        freq[1] = 0

    if result % 2 == 0:
        result -= 1

    for key in freq:
        count: int = 0
        curr: int = key
        while freq.get(curr, 0) > 1:
            count += 2
            curr *= curr

        result = max(result, count + (1 if curr in freq else -1))
        
    return result
    

def main() -> None:
    print("3020. Find the Maximum Number of Elements in Subset")
    print(f"Result: {maximumLength([5,4,1,2,2])}")


if __name__ == "__main__":
    main()