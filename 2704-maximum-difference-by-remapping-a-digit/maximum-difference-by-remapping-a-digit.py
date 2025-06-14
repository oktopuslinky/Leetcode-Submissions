class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        numStr = list(str(num))
        for firstNonNine in numStr:
            if firstNonNine != '9':
                break
        firstDigit = numStr[0]
        maxNum = numStr[:]
        minNum = numStr[:]
        for i, digit in enumerate(numStr):
            if digit == firstNonNine:
                maxNum[i] = '9'
            if digit == firstDigit:
                minNum[i] = '0'

        return int("".join(maxNum)) - int("".join(minNum))