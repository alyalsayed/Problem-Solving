class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Initialize an array to store the frequencies of digits in the secret and guess strings
        freq = [0] * 10
        
        # Initialize two counters for the number of bulls and cows
        bulls = 0
        cows = 0
        
        # Iterate over the digits in the secret and guess strings
        for i in range(len(secret)):
            # If the digit at the same position in the secret and guess strings is the same, increment the bulls counter
            if secret[i] == guess[i]:
                bulls += 1
            else:
                # Otherwise, increment the frequency of the digit in the freq array
                freq[int(secret[i])] += 1
                freq[int(guess[i])] -= 1
        
        # Iterate over the frequencies in the freq array and increment the cows counter
        # by the absolute value of the frequency of the digit
        for f in freq:
            cows += abs(f)
        
        # Build and return the result string in the format "XAYB", where X is the number of bulls and Y is the number of cows
        return str(bulls) + "A" + str(cows//2) + "B"
