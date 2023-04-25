class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the indices of the numbers
        indices = {}
        
        # Iterate over the numbers in the list
        for i, num in enumerate(nums):
            # Calculate the complement of the current number with respect to the target
            complement = target - num
            
            # If the complement is already in the dictionary, we have found a pair of numbers that add up to the target
            if complement in indices:
                return [indices[complement], i]
            
            # Otherwise, add the index of the current number to the dictionary
            indices[num] = i
        
        # If no pair of numbers adds up to the target, return an empty list
        return []