#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
public:
    static int NumberOfSubStrings(const std::string &str) {
        std::unordered_map<char, int> frequency {
            {'a', 0},
            {'b', 0},
            {'c', 0}
        };

        const int n = static_cast<int>(str.length());

        int count { 0 };
        int p1 { 0 };

        for (int p2 { 0 }; p2 < n; p2++) {
            if (str.at(p2) == 'a' || str.at(p2) == 'b' || str.at(p2) == 'c') {
                frequency.at(str.at(p2))++;

                while (frequency.at('a') > 0 && frequency.at('b') > 0 && frequency.at('c') > 0) {
                    count += n - p2;

                    frequency.at(str.at(p1))--;
                    p1++;
                }
            }
        }

        return count;
    }
};

int main() {
    std::cout << "1358. Number of Substrings Containing All Three Characters"<< std::endl;
    std::string abc {"abcabc"};

    const int count { Solution::NumberOfSubStrings(abc) };
    std::cout << count << std::endl;
}