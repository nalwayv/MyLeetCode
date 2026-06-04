#include<string>

class Solution {
public:
    int totalWaviness(int num1, int num2) {
        int result = 0;
        for(int i = num1; i <= num2; i++) {
            std::string num = std::to_string(i);
            if (num.size() < 3)
                continue;

            int count = 0;
            for(int j = 0; j <= num.size() - 3; j++) {
                auto current = num.substr(j, 3);
                if ((current[1] > current[0] && current[1] > current[2]) ||
                    (current[1] < current[0] && current[1] < current[2])){
                    count++;
                }
            }
            
            result += count;
        }

        return result;
    }
};
