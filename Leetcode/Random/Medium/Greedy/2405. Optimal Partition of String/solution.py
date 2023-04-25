class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s) # get the length of the input string
        m = {} # initialize an empty dictionary to keep track of characters in current substring
        ans = 1 # initialize count to 1 (we can always take the whole string as a substring)
        for i in range(n): # loop through all indices in the input string
            if s[i] in m: # check if current character has already appeared in current substring
                ans += 1 # increment count (we need to make a cut here to start a new substring)
                m.clear() # clear dictionary to start a new substring
            m[s[i]] = i # mark current character as seen by adding it to dictionary with its index
           
        
        return ans # return number of substrings