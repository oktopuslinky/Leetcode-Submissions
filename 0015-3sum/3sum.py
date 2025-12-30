class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        nums.sort()

        #print nums

        for i, num in enumerate(nums[:-2]):
            target = -num
            l, r = i+1, len(nums)-1
            while l < r:
                #print nums[i], nums[l], nums[r]
                if nums[l] + nums[r] > target:
                    #print(l, r, target, '>')
                    r -= 1
                if nums[l] + nums[r] < target:
                    #print(l, r, target, '<')
                    l += 1
                if nums[l] + nums[r] == target and l != r:
                    to_add = [nums[i], nums[l], nums[r]]
                    if to_add not in triplets:
                        triplets.append(to_add)
                    l += 1
                    r -= 1
        return triplets