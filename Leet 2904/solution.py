def shortest_beautiful_substring(s: str, k: int) -> str:
    counter: dict[str, int] = {"0": 0, "1": 0}
    n: int = len(s)

    result_len: int = -1
    result_str: str = ""

    p1: int = 0
    for p2 in range(n):
        counter[s[p2]] = counter.get(s[p2], 0) + 1

        while p1 < p2 and counter["1"] > k:
            counter[s[p1]] -= 1
            p1 += 1

        if counter["1"] == k:
            beautiful_str: str = s[p1 : p2 + 1].lstrip("0")
            beautiful_len: int = len(beautiful_str)
            print(beautiful_str)
            
            if result_len == -1:
                result_len = beautiful_len
                result_str = beautiful_str
            elif (beautiful_len, beautiful_str) < (result_len, result_str):
                result_len = beautiful_len
                result_str = beautiful_str

    return result_str

def main() -> None:
    print(shortest_beautiful_substring("100011001", 3))

if __name__ == "__main__":
    main()