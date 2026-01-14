class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) < 2:
            return len(s)

        seen = set()
        left_index = 0
        seen.add(s[left_index])
        max_len = 0
        for right_index in range(1, len(s)):
            while s[right_index] in seen:
                seen.remove(s[left_index])
                left_index += 1

            seen.add(s[right_index])
            max_len = max(max_len, right_index-left_index+1)
        return max_len