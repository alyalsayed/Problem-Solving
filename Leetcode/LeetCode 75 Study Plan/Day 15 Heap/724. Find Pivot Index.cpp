class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int len = nums.size();
        long long sumleft = 0;
        long long sumright = 0;
        for (int j = len - 1; j >= 0 ; j--) {
            sumright += nums[j];
        }
        int i = 0;
        while (i < len) {
             
            if (i == 0) {
                sumleft += 0;
            } else {
                sumleft += nums[i - 1];
            }
            sumright -= nums[i]; 
            if (sumleft == sumright) {
                return i;
            }
            i++;
           
        }
        return -1;
    }
};