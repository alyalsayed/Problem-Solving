class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m=text1.size();int n=text2.size();
        return lcs(text1,text2,m,n) ;
    }
int lcs(string X, string Y, int m, int n)
{
    // intitalizing a matrix of size (m+1)*(n+1)
    int L[m + 1][n + 1];
  
    /* Following steps build L[m+1][n+1] in bottom up fashion. Note
        that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] */
    for (int i = 0; i <= m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (i == 0 || j == 0)
                L[i][j] = 0;
  
            else if (X[i - 1] == Y[j - 1])
                L[i][j] = L[i - 1][j - 1] + 1;
  
            else
                L[i][j] = max(L[i - 1][j], L[i][j - 1]);
        }
    }
  
    // L[m][n] contains length of LCS for X[0..n-1] and Y[0..m-1] 
    return L[m][n];
}
};