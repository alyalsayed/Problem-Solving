#https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert the characters in s to their corresponding numbers
        nums = [str(ord(c) - ord('a') + 1) for c in s]
        # Concatenate the numbers to form a single string
        s = ''.join(nums)
        
        # Perform the required number of transformations
        for i in range(k):
            # Calculate the sum of the digits in s
            sm = sum(int(d) for d in s)
            # Convert the sum to a string
            s = str(sm)
        
        # Return the final sum
        return sm