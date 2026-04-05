class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ''

        length: int = len(encodedText)
        cols: int = length // rows
        
        # build matrix
        matrix: list[list[str]] = []
        for i in range(0, length, cols):
            matrix.append([c for c in encodedText[i:i+cols]])

        # decode
        builder: list[str] = []
        for i in range(cols):
            for r in range(rows):
                if i >= cols:
                    break
                builder.append(matrix[r][i])
                i += 1

        return ''.join(builder).rstrip()
    

def main() -> None:
    print('2075. Decode the Slanted Ciphertext')

    solution = Solution()
    case1_result = solution.decodeCiphertext('ch   ie   pr', 3)
    print(case1_result)


if __name__ == '__main__':
    main()