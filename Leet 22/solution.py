class Solution:
    def _backtrack(
            self, 
            result: list[str],
            n: int,
            str_builder: str,
            open_parenthesis: int= 0,
            close_parenthesis: int= 0) -> None:
        """
        Recursively generates all combinations of parentheses for a given number of pairs.
        Args:
            result (list[str]): The list to store valid parentheses combinations.
            n (int): The total number of pairs of parentheses.
            str_builder (str): The current string being built.
            open_parenthesis (int, optional): The count of open parentheses used so far. Defaults to 0.
            close_parenthesis (int, optional): The count of close parentheses used so far. Defaults to 0.
        Returns:
            None: The function modifies the result list in place.
        """        
        if len(str_builder) == n*2:
            result.append(str_builder)
            return
        
        # add open parenthesis
        if open_parenthesis < n:
            str_builder += '('
            self._backtrack(result, n, str_builder, open_parenthesis + 1, close_parenthesis)
            str_builder = str_builder[:-1]

        # add close parenthesis
        if close_parenthesis < open_parenthesis:
            str_builder += ')'
            self._backtrack(result, n, str_builder, open_parenthesis, close_parenthesis + 1)
            str_builder = str_builder[:-1]


    def generate_parenthesis(self, n: int) -> list[str]:
        """
        Generates all combinations of parentheses for a given number of pairs.

        Args:
            n (int): The number of pairs of parentheses.

        Returns:
            list[str]: A list containing all valid combinations of n pairs of parentheses.
        """
        result: list[str] = []
        str_builder: str = ''
        self._backtrack(result, n, str_builder)
        return result


def main() -> None:
    print('22. Generate Parentheses')

    sol = Solution()
    print('case 1 with 3n pairs')
    for case1 in sol.generate_parenthesis(3):
        print(f'{'':>2}- {case1}')


if __name__ == '__main__':
    main()