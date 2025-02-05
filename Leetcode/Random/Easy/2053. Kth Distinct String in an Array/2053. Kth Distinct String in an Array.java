class Solution {
      public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> frequency = new HashMap<>();
        
        for (String s : arr) {
            frequency.put(s, frequency.getOrDefault(s, 0) + 1);
        }
        
        
        int count = 0;
        for (String s : arr) {
            if (frequency.get(s) == 1) {
                count++;
                if (count == k) {
                    return s;
                }
            }
        }
        return "";
    }
}