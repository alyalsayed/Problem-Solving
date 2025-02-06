class Solution {
   private Map<Integer, Integer> memo = new HashMap<>();

    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        return Math.min(helper(cost, n - 1), helper(cost, n - 2));
    }

    private int helper(int[] cost, int i) {
        if (i < 0) return 0;
        if (i == 0 || i == 1) return cost[i];

        if (memo.containsKey(i)) return memo.get(i);

        int result = cost[i] + Math.min(helper(cost, i - 1), helper(cost, i - 2));
        memo.put(i, result);
        return result;
    }
}