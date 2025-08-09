class TextEditor:
    def __init__(self):
        self.left: list[str] = []
        self.right: list[str] = []
        
    def addText(self, text: str) -> None:
        """Appends text to where the cursor is. The cursor ends to the right of text
        """
        for ch in text:
            self.left.append(ch)

    def deleteText(self, k: int) -> int:
        """Deletes k characters to the left of the cursor. Returns the number of characters actually deleted
        """
        removed: int = 0
        while self.left and k > 0:
            self.left.pop()
            k -= 1
            removed += 1

        return removed
    
    def cursorLeft(self, k: int) -> str:
        """Moves the cursor to the left k times
        """
        while self.left and k > 0:
            self.right.append(self.left.pop())
            k -= 1

        length: int = min(10, len(self.left))
        return "".join(self.left[-length:])
    
    def cursorRight(self, k: int) -> str:
        """ Moves the cursor to the right k times
        """
        while self.right and k > 0:
            self.left.append(self.right.pop())
            k -= 1

        length: int = min(10, len(self.left))
        return "".join(self.left[-length:])
    

def main() -> None:
    print("2296. Design a Text Editor")

    txt = TextEditor()

    txt.addText("leetcode")
    print(txt.deleteText(4))
    txt.addText("practice")
    print(txt.cursorRight(3))
    print(txt.cursorLeft(8))
    print(txt.deleteText(10))
    print(txt.cursorLeft(2))
    print(txt.cursorRight(6))


if __name__ == "__main__":
    main()

