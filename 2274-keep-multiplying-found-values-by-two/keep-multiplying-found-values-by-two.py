class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums = set(nums)        
        for num in nums:
            if original in nums:
                original *= 2
            else:
                return original
        return original