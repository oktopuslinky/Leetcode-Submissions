class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sum = max(cur_sum, max_sum)
        return max_sum