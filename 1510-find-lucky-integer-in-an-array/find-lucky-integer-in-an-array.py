class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        freqs = {}
        for integer in arr:
            freqs[integer] = freqs.get(integer, 0) + 1
        
        for integer, freq in reversed(list(freqs.items())):
            if integer == freq:
                return integer
                        
        return -1