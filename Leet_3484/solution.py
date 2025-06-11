import re


class Spreadsheet:
    def __init__(self, rows: int):
        self.abc: str = "abcdefghijklmnopqrstuvwxyz"
        self.table: dict[str, int] = {}

    def setCell(self, cell: str, value: int) -> None:
        """
        Sets the value of a specified cell in the spreadsheet.

        Args:
            cell (str): The cell identifier.
        """
        normal: str = cell.lower()

        # Validate row (letter) and column (number)
        if normal[0].isalpha() or not normal[1:].isdigit():
            return

        self.table[normal] = value
        
    def resetCell(self, cell: str) -> None:
        """
        Resets the value of the specified cell to 0.

        Args:
            cell (str): The cell identifier
        """
        normal: str = cell.lower()
        if normal in self.table:
            self.table[normal] = 0

    def getValue(self, formula: str) -> int:
        """
        Evaluates a spreadsheet formula in the form of '=X+Y' and returns its int value.

        Args:
            formula (str): The formula string to evaluate.
        
        Returns:
            int: The computed value of the formula, or -1 if the formula does not start with '='.
        """
        normal: str = formula.lower()
        if normal[0] != "=":
            return -1

        number: int = 0
        for x in re.split(r'[\=\+\-\*/]', normal):
            if x in self.table:
                number += self.table[x]
            elif x.isdecimal():
                number += int(x)
    
        return number


def main() -> None:
    print("3484. Design Spreadsheet")

    ss = Spreadsheet(3)
    print("Get", ss.getValue("=5+7"))       # returns 12 (5+7)
    ss.setCell("A1", 10)                    # sets A1 to 10
    print("Get", ss.getValue("=A1+6"))      # returns 16 (10+6)
    ss.setCell("B2", 15)                    # sets B2 to 15
    print("Get", ss.getValue("=A1+B2"))     # returns 25 (10+15)
    ss.resetCell("A1")                      # resets A1 to 0
    print("Get", ss.getValue("=A1+B2"))     # returns 15 (0+15)


if __name__ == "__main__":
    main()