from itertools import zip_longest

class Solution:
    def _clean_up(self, s: str) -> list[str]:
        """
        Splits a version string by '.' and removes leading zeros from each segment.

        Args:
            s (str): The version string to clean up.

        Returns:
            list[str]: A list of string segments with leading zeros removed.
        """
        result: list[str] = []
        for ch in s.split('.'):
            # remove leading zero's if any
            if ch[0] == '0' and len(ch) > 1:
                left: int = 0
                while left + 1 < len(ch) and ch[left] == '0':
                    left += 1
                result.append(ch[left:])
            else:
                result.append(ch)
        return result

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Compares two version numbers given as strings.
        Each version string consists of numbers separated by dots (e.g., "1.2.3").
        The comparison is performed by splitting the version strings into their numeric components,
        normalizing their lengths by filling missing components with '0', and comparing each component
        as an integer from left to right.
        Args:
            version1 (str): The first version string to compare.
            version2 (str): The second version string to compare.
        Returns:
            int: 
                -1 if version1 < version2,
                 1 if version1 > version2,
                 0 if both versions are equal.
        """
        v1_cleaned_up: list[str] = self._clean_up(version1)
        v2_cleaned_up: list[str] = self._clean_up(version2)

        for value1, value2 in zip_longest(v1_cleaned_up, v2_cleaned_up, fillvalue= '0'):
            if value1 == value2:
                continue

            if int(value1) < int(value2):
                return -1
            
            if int(value1) > int(value2):
                return 1

        return 0


def main() -> None:
    print('165. Compare Version Numbers')

    solution = Solution()

    print(f'case 1 should equal -1 ? {solution.compareVersion('1.2', '1.10')}')
    print(f'case 2 should equal 0 ? {solution.compareVersion('1.01', '1.001')}')
    print(f'case 3 should equal 0 ? {solution.compareVersion('1.0', '1.0.0.0')}')


if __name__ == '__main__':
    main()