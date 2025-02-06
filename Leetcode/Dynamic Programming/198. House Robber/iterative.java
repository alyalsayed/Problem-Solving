class Solution {
   public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int prev1 = 0; 
        int prev2 = 0;  

        for (int num : nums) {
            int temp = prev1;
            prev1 = Math.max(prev1, num + prev2);
            prev2 = temp;
        }

        return prev1;
    }
}