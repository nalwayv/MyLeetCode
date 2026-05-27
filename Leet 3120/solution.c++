#include <array>

class Solution {
public:
    // 3120. Count the Number of Special Characters I
    int numberOfSpecialChars(string word) {
        std::array<bool, 26> lower{false};
        std::array<bool, 26> upper{false};

        for (const auto &c: word) {
            int lower_index = c - 'a';
            if (lower_index >= 0 && lower_index < 26) {
                lower[lower_index] = true;
            }

            int upper_index = c - 'A';
            if (upper_index >= 0 && upper_index < 26) {
                upper[upper_index] = true;
            }
        }

        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lower[i] && upper[i]) {
                count++;
            }
        }
        
        return count;
    }
};