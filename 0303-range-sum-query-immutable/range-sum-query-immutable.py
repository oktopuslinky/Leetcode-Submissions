class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefixes = [nums[0]]

        if len(nums) == 1:
            return

        for num in nums[1:]:
            self.prefixes.append(self.prefixes[-1]+num)
        print self.prefixes

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefixes[right]
        return self.prefixes[right] - self.prefixes[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)