class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        repeats = []
        for num in nums:
            if num in seen:
                repeats.append(num)
            seen.add(num)

        return repeats