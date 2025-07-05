class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freqs = {}
        for integer in arr:
            freqs[integer] = freqs.get(integer, 0) + 1
        
        largest_lucky = -1
        for integer, freq in reversed(list(freqs.items())):
            if integer == freq:
                return integer
                #largest_lucky = max(largest_lucky, integer)
        
        return largest_lucky