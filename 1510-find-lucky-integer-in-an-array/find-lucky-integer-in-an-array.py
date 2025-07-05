class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freqs = {}
        for integer in arr:
            freqs[integer] = freqs.get(integer, 0) + 1
        
        for integer in reversed(freqs.keys()) :
            if integer == freqs[integer]:
                return integer
        
        return -1