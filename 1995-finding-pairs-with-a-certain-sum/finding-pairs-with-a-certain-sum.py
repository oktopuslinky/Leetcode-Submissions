class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = {}
        for num in nums1:
            if num in self.nums1:
                self.nums1[num] += 1
            else:
                self.nums1[num] = 1
            #self.nums1[num] = self.nums1.get(num, 0) + 1
        self.nums2 = nums2
        self.nums2Count = {}
        for num in nums2:
            if num in self.nums2Count:
                self.nums2Count[num] += 1
            else:
                self.nums2Count[num] = 1
            #self.nums2Count[num] = self.nums2Count.get(num, 0) + 1

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        #print index, val, self.nums2
        changeVal = self.nums2[index]
        self.nums2Count[changeVal] -= 1
        changeVal += val
        self.nums2[index] = changeVal
        if changeVal in self.nums2Count:
            self.nums2Count[changeVal] += 1
        else:
            self.nums2Count[changeVal] = 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        output = 0

        for num, count in self.nums1.items():
            to_find = tot-num
            if to_find in self.nums2Count:
                output += self.nums1[num] * self.nums2Count[to_find]
        return output
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)