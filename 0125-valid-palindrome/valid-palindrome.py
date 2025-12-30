class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l, r = 0, len(s)-1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            #print l, r, s[l], s[r]
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True