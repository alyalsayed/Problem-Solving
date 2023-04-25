# https://leetcode.com/problems/remove-letter-to-equalize-frequency/


from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # If all characters in the word are distinct, then it is not possible to remove a character
        if len(word) == len(set(word)):
            return True
        
        # Convert the string to a list to be able to remove elements from it
        word_list = list(word)
        
        # Iterate through each  character in the list and try removing the character 
        for index, char in enumerate(word_list):
            # If the character occurs more than once in the word, remove it and check if the frequencies are equal
            if word_list.count(char) > 0:
                word_list.pop(index)
                freq_values = Counter(word_list).values()
                if len(set(freq_values)) == 1:
                    return True
                else:
    # If the frequencies are not equal, insert the character back and try the next character
                    word_list.insert(index, char)
        
        # If no character can be removed to make the frequencies equal, return False
        return False