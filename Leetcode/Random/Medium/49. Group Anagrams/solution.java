class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramMap = new HashMap<>();
        
        for (String str : strs) {
           
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            
            
            anagramMap.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }
       
        return new ArrayList<>(anagramMap.values());
    }
}