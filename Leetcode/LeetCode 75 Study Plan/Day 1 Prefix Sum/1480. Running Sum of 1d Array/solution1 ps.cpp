class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        //prefix sum
        vector<int> sum_result(nums.size());
        sum_result[0]=nums[0];
        for(int i = 1 ; i< nums.size(); i++ ){
             sum_result[i]+= sum_result[i-1]+nums[i];
    }
    return sum_result;
    }
};