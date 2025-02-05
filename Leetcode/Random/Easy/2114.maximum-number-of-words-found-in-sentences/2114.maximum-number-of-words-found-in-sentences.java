class Solution {
    public int mostWordsFound(String[] sentences) {
         int mostWordsFound = 0;
        for (String sentence : sentences) {
            String[] words = sentence.split(" ");
            mostWordsFound = (mostWordsFound > words.length)?mostWordsFound:words.length;
        }
        return mostWordsFound;
    }
}