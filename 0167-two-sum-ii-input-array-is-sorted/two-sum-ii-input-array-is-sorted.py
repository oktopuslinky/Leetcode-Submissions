class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}
        for i, num in enumerate(numbers):
            goal = target-num
            if goal in seen:
                return [seen[goal]+1, i+1]
            seen[num] = i