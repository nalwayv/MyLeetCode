# Ransom Note
#
# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
#
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
#
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import defaultdict


def can_construct(ransomNote: str, magazine: str) -> bool:
    # get chars from magazine and store count

    letters: dict[str, int] = defaultdict(int)
    for char in magazine:
        letters[char] += 1

    # check chars in ransomNote and see 
    # if they are in letters and the count is more the zero

    for char in ransomNote:
        if char not in letters:
            return False
        
        if letters[char] <= 0:
            return False
            
        letters[char] -= 1
       
    return True


def main() -> None:
    print(can_construct("a", "b") == False)
    print(can_construct("aa", "ab") == False)
    print(can_construct("aa", "aab") == True)
    print(can_construct("leetcode", "tlecodee") == True)


if __name__ == "__main__":
    main()