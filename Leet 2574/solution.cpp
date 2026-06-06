#include <algorithm>
#include <cstdlib>

class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        std::vector<int> result(nums.size());
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        
        int left_sum = 0;
        for(int i = 0; i < nums.size(); i++) {
            total -= nums[i];

            if (left_sum >= total) 
                result[i] = left_sum - total;
            else
                result[i] = total - left_sum;

            left_sum += nums[i];
        }

        return result;
    }
};