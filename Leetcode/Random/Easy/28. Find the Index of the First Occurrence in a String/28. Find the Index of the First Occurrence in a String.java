class Solution {
    public int strStr(String haystack, String needle) {
       return haystack.contains(needle) ? haystack.indexOf(needle) : -1 ;
    }
}