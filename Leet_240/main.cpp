#include <iostream>
#include <vector>
#include <format>

// ----------------------------------------------------------------------------------
namespace Leet
{
    // ----------------------------------------------------------------------------------
    class Solution
    {
    public:
        bool SearchMatrix(std::vector<std::vector<int>> &matrix, int target);
    };

    // ----------------------------------------------------------------------------------
    bool Solution::SearchMatrix(std::vector<std::vector<int>> &matrix, int target)
    {
        // Example:
        // t = 3
        // start bottom left
        // 1)
        //      0  1  2
        //   0[ 1  2  3 ]
        //   1[ 4  5  6 ]
        //   2[[7] 8  9 ]
        //   7 > t: r--
        // 2)
        //      0  1  2
        //   0[ 1  2  3 ]
        //   1[[4] 5  6 ]
        //   2[ 7  8  9 ]
        //   4 < t: c++
        // 3)
        //      0  1  2
        //   0[ 1  2  3 ]
        //   1[ 4 [5] 6 ]
        //   2[ 7  8  9 ]
        //   5 == t

        int row = matrix.size() - 1;
        int col = 0;

        while (row >= 0 && col < matrix[0].size())
        {
            if (matrix[row][col] == target)
            {
                return true;
            }

            if (matrix[row][col] < target)
            {
                col++;
            }
            else
            {
                row--;
            }
        }

        return false;
    }
}

// ----------------------------------------------------------------------------------
static void Case1(Leet::Solution &solution)
{
    std::vector<std::vector<int>> matrix = {
        {1, 4, 7, 11, 15},
        {2, 5, 8, 12, 19},
        {3, 6, 9, 16, 22},
        {10, 13, 14, 17, 24},
        {18, 21, 23, 26, 30}};

    bool result = solution.SearchMatrix(matrix, 5);
    std::cout << std::format("Case 1: {}\n", (result ? "Pass" : "Fail"));
}

// ----------------------------------------------------------------------------------
static void Case2(Leet::Solution &solution)
{
    std::vector<std::vector<int>> matrix = {
        {1, 4, 7, 11, 15},
        {2, 5, 8, 12, 19},
        {3, 6, 9, 16, 22},
        {10, 13, 14, 17, 24},
        {18, 21, 23, 26, 30}};

    bool result = solution.SearchMatrix(matrix, 20);
    std::cout << std::format("Case 2: {}\n", (!result ? "Pass" : "Fail"));
}

// ----------------------------------------------------------------------------------
static void Case3(Leet::Solution &solution)
{
    std::vector<std::vector<int>> matrix = {{-5}};

    bool result = solution.SearchMatrix(matrix, -5);
    std::cout << std::format("Case 3: {}\n", (result ? "Pass" : "Fail"));
}

// ----------------------------------------------------------------------------------
int main()
{
    std::cout << "240. Search a 2D Matrix II\n";

    Leet::Solution solution{};

    Case1(solution);
    Case2(solution);
    Case3(solution);
}