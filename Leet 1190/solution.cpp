#include <iostream>
#include <vector>

namespace {
    class Solution {
    public:
        static std::string reverse_parentheses(const std::string& str) {
            std::vector<std::string> builder;
            const std::string start {"("};

            for (const auto ch: str) {
                if (ch == ')') {
                    std::vector<std::string> reversed;
                    while (builder.back() != start) {
                        reversed.push_back(builder.back());
                        builder.pop_back();
                    }

                    builder.pop_back();
                    
                    builder.insert(builder.end(), reversed.begin(), reversed.end());
                } else {
                    builder.push_back(((std::string){ch}));
                }
            }

            std::string result;
            for (const auto & b_str : builder) {
                result += b_str;
            }
            return result;
        }
    };
}

int main() {
    const std::string result = Solution::reverse_parentheses("(ed(et(oc))el)");
    std::cout << "Result: " << result << std::endl;
    return 0;
}
