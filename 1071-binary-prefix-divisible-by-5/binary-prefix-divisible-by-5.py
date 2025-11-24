class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        output = []
        x_i = 0
        for i in range(len(nums)):
            x_i = (x_i << 1) | nums[i]
            if x_i % 5 == 0:
                output.append(True)
            else:
                output.append(False)
        
        return output