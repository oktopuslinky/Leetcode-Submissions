class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        # sorted elements

        nums.sort()
        output = []
        groupNum = 0
        while groupNum < len(nums)/3:
            to_append = nums[groupNum*3:groupNum*3+3]
            print to_append
            print to_append[1] - to_append[0]
            print to_append[2] - to_append[1]
            print to_append[2] - to_append[0]
            if to_append[1] - to_append[0] <= k and to_append[2] - to_append[1] <= k and to_append[2] - to_append[0] <= k:
                output.append(to_append)
            else:
                return []
            groupNum += 1

        return output