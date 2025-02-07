class Solution {
    public int coinChange(int[] coins, int amount) {
          return minChange(amount, coins, new HashMap<>());
    }
     public static int minChange(int amount, int[] coins, HashMap<Integer, Integer> memo) {
        if (amount == 0) {
            return 0;
        }

        if (amount < 0) {
            return -1;
        }

        if (memo.containsKey(amount)) {
            return memo.get(amount);
        }

        int minCoins = -1;
        for (int coin : coins) {
            int subAmount = amount - coin;
            int subCoins = minChange(subAmount, coins, memo);
            
            if (subCoins != -1) {
                int numCoins = subCoins + 1;
                if (minCoins == -1 || numCoins < minCoins) {
                    minCoins = numCoins;
                }
            }
        }

        memo.put(amount, minCoins);
        return minCoins;
    }
}