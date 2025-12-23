class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            if target-num in nums_dict:
                return [i, nums_dict[target-num]]
            nums_dict[num] = i