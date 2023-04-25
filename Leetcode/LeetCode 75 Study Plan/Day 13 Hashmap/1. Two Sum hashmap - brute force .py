class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate over all possible pairs of numbers in the list
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # If the sum of the pair of numbers is equal to the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # If no pair of numbers adds up to the target, return an empty list
        return []