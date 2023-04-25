class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize a hashmap to store the frequencies of characters in the sliding window
        window_freq = {}
        max_freq = 0
        left = 0
        result = 0
        
        # Slide the window over the input string s
        for right in range(len(s)):
            # Increment the frequency of the character at the right end of the window in the window_freq hashmap
            if s[right] in window_freq:
                window_freq[s[right]] += 1
            else:
                window_freq[s[right]] = 1
            
            # Update the maximum frequency of any character in the window
            max_freq = max(max_freq, window_freq[s[right]])
            
            # If the number of characters that need to be changed is greater than k,
            # slide the window to the right and decrement the frequency of the character at the left end of the window
            if right - left + 1 - max_freq > k:
                window_freq[s[left]] -= 1
                left += 1
            
            # Update the length of the longest substring containing the same letter
            result = max(result, right - left + 1)
        
        return result
