class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        nums_count = {}

        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        
        nums_count = sorted(nums_count.items(), key = lambda x: x[1], reverse=True)
        return [num[0] for num in nums_count[:k]]