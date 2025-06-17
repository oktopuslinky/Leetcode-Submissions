class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # if you find smaller element, then record 
        #previous max - min and make max None and min current

        minimum = nums[0]
        maxDiff = -1
        for num in nums[1:]:
            if num > minimum:
                maxDiff = max(maxDiff, num-minimum)
            minimum = min(minimum, num)
        
        return maxDiff