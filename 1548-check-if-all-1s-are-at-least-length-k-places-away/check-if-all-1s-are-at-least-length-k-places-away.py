class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        distance = 0
        found = False # if 1 has been found yet

        for i in range(len(nums)):
            if nums[i] == 0:
                distance += 1
            else:
                if found and distance < k:
                    print(i, distance)
                    return False
                distance = 0
                found = True
        return True