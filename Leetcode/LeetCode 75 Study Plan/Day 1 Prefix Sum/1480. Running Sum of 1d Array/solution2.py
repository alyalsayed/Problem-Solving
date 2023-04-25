class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_total = 0
        running_sum = []
        for num in nums:
            running_total += num
            running_sum.append(running_total)
        return running_sum