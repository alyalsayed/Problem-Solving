class Solution {
    public int countVowelSubstrings(String word) {
        int vowelCount = 0;

        for (int i = 0; i < word.length(); i++) {
            char current = word.charAt(i);

            if (isVowel(current)) {
                for (int j = i ; j < word.length(); j++) {
                    String currentSubstring = word.substring(i, j);

                    if (containsAllVowels(currentSubstring)) {
                        System.out.println(currentSubstring);
                        vowelCount++;
                    }
                }
            }
           
        }
         return vowelCount;
    }
    
    public static boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    public static boolean containsAllVowels(String word) {
        return word.contains("a") && word.contains("e") && word.contains("i") && word.contains("o") && word.contains("u");
    }
}