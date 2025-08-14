class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        largest = -1
        for i, number in enumerate(num[2:]):
            print i, number
            if number == num[i] and num[i] == num[i+1]:
                largest = max(largest, int(number))
        
        if largest != -1:
            return 3 * str(largest)
        else:
            return ""