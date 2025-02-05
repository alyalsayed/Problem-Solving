class Solution {
    public int lengthOfLastWord(String s) {
        String trimmed = s.trim();
        String[] splitted = trimmed.split(" ");
        String last = splitted[splitted.length - 1];
        return last.length();
    }
}