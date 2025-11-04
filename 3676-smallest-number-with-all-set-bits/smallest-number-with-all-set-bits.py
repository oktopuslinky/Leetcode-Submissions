class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        multiplier = 1
        bin_num = 1

        while bin_num < n:
            multiplier *= 2
            bin_num += multiplier

        return bin_num