class Solution {
    public char findTheDifference(String s, String t) {
        int r1=0,r2=0;
        for(char c : s.toCharArray()) {
            r1+=(int)c;
        }
        for(char c : t.toCharArray()) {
            r2+=(int)c;
        }
        int r3= (r2 > r1 )? (r2 - r1): (r2-r2);
        return (char)r3 ;
    }
}