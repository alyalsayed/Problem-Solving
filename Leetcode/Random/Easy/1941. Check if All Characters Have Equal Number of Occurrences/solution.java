class Solution {
    public boolean areOccurrencesEqual(String s) {
         int[] freq = new int[26];  
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }      
        int targetFreq = 0;
        for (int f : freq) {
            if (f > 0) {
                targetFreq = f;
                break;
            }
        }

    
        for (int f : freq) {
            if ( f > 0 && f != targetFreq) {
                return false;  
            }
        }
        
        return true;  
    }
}