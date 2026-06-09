class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        if (nums.size() == 0) { 
            return 0; 
        }

        int min { nums.at(0) };
        int max { nums.at(0) };

        for(int i { 1 }; i < nums.size(); i++) {
            auto current { nums.at(i) };
            
            if (current > max) { 
                max = current; 
            }
            if (current < min) { 
                min = current; 
            }
        }
        
        return (long long)(max - min) * k;
    }
};