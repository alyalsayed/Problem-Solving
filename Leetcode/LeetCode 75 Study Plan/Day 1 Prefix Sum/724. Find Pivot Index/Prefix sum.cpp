class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int len = nums.size();
        vector<int> prefix_sum(len + 1, 0);
        vector<int> suffix_sum(len + 1, 0);
        for (int i = 1; i <= len; i++) {
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1];
        }
        for (int i = len-1; i >= 0; i--) {
            suffix_sum[i] = suffix_sum[i+1] + nums[i];
        }
        for (int i = 0; i < len; i++) {
            if (prefix_sum[i] == suffix_sum[i+1]) {
                return i;
            }
        }
        return -1;
    }
};