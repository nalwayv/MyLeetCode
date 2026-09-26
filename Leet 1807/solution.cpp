// 1807. Evaluate the Bracket Pairs of a String

#include <iostream>
#include <unordered_map>
#include <vector>

using Knowledge = std::vector<std::vector<std::string>>;
using Replacements = std::unordered_map<std::string, std::string>;

static std::string evaluate(const std::string &input, const Knowledge& knowledge) {
    Replacements key_replacements;
    for (const auto &pair : knowledge) {
        if (pair.size() != 2) {
            continue;
        }
        key_replacements[pair[0]] = pair[1];
    }

    std::string result;

    int start = 0;
    while (start < input.size()) {
        if (input.at(start) == '(') {
            int end = start + 1;

            while (end < input.size() && input.at(end) != ')') {
                end++;
            }

            auto slice = input.substr(start + 1, end - start - 1);
            result += key_replacements.contains(slice) ? key_replacements.at(slice) : "?";

            start = end + 1;
        } else {
            result += input.at(start);
            start++;
        }
    }

    return result;
};