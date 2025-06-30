class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        max_length = 0
        
        # Check each number in the frequency counter
        for num in count:
            # If num + 1 exists, check if their combined frequency is larger
            if num + 1 in count:
                current_length = count[num] + count[num + 1]
                max_length = max(max_length, current_length)
        
        return max_length