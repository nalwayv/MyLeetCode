import math

def generate_parenthesis(n: int) -> list[str]:
    if n <= 0 or n > 8:
        return []
    
    str_builder: list[str] = [""] * (n * 2)
    result: list[str] = []

    def bk(i: int, o: int, c: int):
        if i == (n * 2):
            result.append("".join(str_builder))
            return
        
        if o < n:
            str_builder[i] = "("
            bk(i + 1, o + 1, c)

        if c < o:
            str_builder[i] = ")"
            bk(i + 1, o, c + 1)
    
    bk(0, 0, 0)
    
    return result


def catalan(n: int):
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))


def main() -> None:
    print('22. Generate Parentheses')

    pairs: list[str] = generate_parenthesis(8)

    print("Case generate_parenthesis(8)")
    for case1 in pairs:
        print(f'{'':>2}- {case1}')


if __name__ == '__main__':
    main()