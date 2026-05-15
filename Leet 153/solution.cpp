class Solution {
public:
    int findMin(vector<int>& nums) {
        int result = nums[0];

        for(int i = 0; i < static_cast<int>(nums.size()) - 1; i++) {
            if (nums[i + 1] - nums[i] < 0) {
                result = std::min(result, nums[i + 1]);
            }
        }
        
        return result;
    }
};

int main() {
    Solution solution;

    std::vector nums = {3,4,5,1,2};
    std::cout << solution.FindMin(nums) << "\n";
    std::cout << "END!" << std::endl;
}