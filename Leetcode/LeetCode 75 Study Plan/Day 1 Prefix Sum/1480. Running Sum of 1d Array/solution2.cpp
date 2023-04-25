class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        
        int running_total = 0;
        vector<int> running_sum;

        for (int num : nums) {
            running_total += num;
            running_sum.push_back(running_total);
        }

        return running_sum;
        }
};