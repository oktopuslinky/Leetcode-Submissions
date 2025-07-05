class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort(reverse=True)
        curNum = -1
        curCount = 0
        for num in arr:
            if num == curNum:
                curCount += 1
            else:
                if curNum == curCount:
                    return curNum
                else:
                    curNum = num
                    curCount = 1
                    
        if curNum == curCount:
            return curNum
        return -1