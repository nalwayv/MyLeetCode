class Solution:
    """
    Given two arrays of strings list1 and list2, find the common strings with the least index sum.

    A common string is a string that appeared in both list1 and list2.

    Example:
        Input: list1 = ["happy","sad","good"]

        list2 = ["sad","happy","good"]

        Output: ["sad","happy"]

    Explanation: 
        There are three common strings:

        "happy" with index sum = (0 + 1) = 1.

        "sad" with index sum = (1 + 0) = 1.

        "good" with index sum = (2 + 2) = 4.

        The strings with the least index sum are "sad" and "happy".
    """
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        table: dict[str, int] = {}
        # Add list 1 to table
        for idx, val in enumerate(list1):
            table[val] = idx

        result: list[str] = []
        lo: int = 0xFFFF

        # Check if list2 values are in tables
        # If yes then check the lo and append if equil else 
        # clear and start again
        for idx, val in enumerate(list2):
            if val in table:
                new_lo: int = table[val] + idx

                if new_lo <= lo:
                    if new_lo == lo:
                        result.append(val)
                    else:
                        if result:
                            result.clear()

                        result.append(val)
                    lo = new_lo
    
        return result


# def from_file():
#     """
#     using text from text_file
#     """
#     list1: list[str] = []
#     with open("./text/leet_599_list1.txt", "r") as f1:
#         list1 = f1.readlines()

#     list2: list[str] = []
#     with open("./text/leet_599_list2.txt", "r") as f1:
#         list2 = f1.readlines()

#     table: dict[str, int] = {}
#     for idx, val in enumerate(list1):
#         table[val] = idx
    
#     for idx, val in enumerate(list2):
#         if val in table:
#             table[val] += idx
    
#     solution = Solution()
#     for result in solution.findRestaurant(list1, list2):
#         print(result.strip())


def main() -> None:
    solution = Solution()

    l1_a: list[str] = ["Shogun","Tapioca Express","Burger King","KFC"]
    l1_b: list[str] = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    r1 = solution.findRestaurant(l1_a, l1_b)
    print(f"Output: {r1}") #shogun

    l2_a: list[str] = ["Shogun","Tapioca Express","Burger King","KFC"]
    l2_b: list[str] = ["KFC","Shogun","Burger King"]
    r2 = solution.findRestaurant(l2_a, l2_b)
    print(f"Output: {r2}")# shogun

    l3_a: list[str] = ["happy","sad","good"]
    l3_b: list[str] = ["sad","happy","good"]
    r3 = solution.findRestaurant(l3_a, l3_b)
    print(f"Output: {r3}")# happy, sad

    # from_file()


if __name__ == "__main__":
    main()