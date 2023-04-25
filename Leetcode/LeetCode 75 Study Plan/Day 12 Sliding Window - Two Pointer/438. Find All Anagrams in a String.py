class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initialize a hashmap to store the frequencies of characters in the pattern string p
        pattern_freq = {}
        for char in p:
            if char in pattern_freq:
                pattern_freq[char] += 1
            else:
                pattern_freq[char] = 1
        
        # Initialize the sliding window parameters
        left = 0
        right = 0
        window_freq = {}
        result = []
        
        # Slide the window over the input string s
        while right < len(s):
            # If the character at the right end of the window is in the pattern string p,
            # increment its frequency in the window_freq hashmap
            if s[right] in pattern_freq:
                if s[right] in window_freq:
                    window_freq[s[right]] += 1
                else:
                    window_freq[s[right]] = 1
            
            # If the window size is greater than the pattern size, slide the window to the right and
            # decrement the frequency of the character at the left end of the window in the window_freq hashmap
            if right - left + 1 > len(p):
                if s[left] in window_freq:
                    window_freq[s[left]] -= 1
                    if window_freq[s[left]] == 0:
                        del window_freq[s[left]]
                left += 1
            
            # If the window size is equal to the pattern size, check if the frequencies of characters
            # in the window_freq hashmap match the frequencies of characters in the pattern_freq hashmap
            if right - left + 1 == len(p):
                if window_freq == pattern_freq:
                    result.append(left)
            
            right += 1
        
        return result