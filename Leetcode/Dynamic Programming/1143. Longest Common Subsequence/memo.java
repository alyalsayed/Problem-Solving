class Solution {
   public static int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        return lcsHelper(text1, text2, m, n, dp);
    }

    private static int lcsHelper(String text1, String text2, int i, int j, int[][] dp) {
        if (i == 0 || j == 0) {
            return 0;
        }
        if (dp[i][j] != -1) {
            return dp[i][j]; 
        }

        if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
            dp[i][j] = 1 + lcsHelper(text1, text2, i - 1, j - 1, dp);
        } else {
            dp[i][j] = Math.max(lcsHelper(text1, text2, i - 1, j, dp),
                                lcsHelper(text1, text2, i, j - 1, dp));
        }

        return dp[i][j];
    }
}