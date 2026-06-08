class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> lo;
        vector<int> hi;

        vector<int> result(nums.size(), pivot);

        int skip { 0 };
        for(int i = 0; i < nums.size(); i++) {
            if (nums.at(i) < pivot) {
                lo.push_back(nums.at(i));
            } else if (nums.at(i) > pivot){
                hi.push_back(nums.at(i));
            } else {
                skip++;
            }
        }

        int idx { 0 };
        for (int num: lo) { 
            result[idx++] = num; 
        }
        
        idx += skip;
        
        for (int num: hi) { 
            result[idx++] = num; 
        }

        return result;
    }
};