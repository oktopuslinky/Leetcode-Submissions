class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_letters, t_letters = {}, {}

        for i in range(len(s)):
            s_letters[s[i]] = s_letters.get(s[i], 0) + 1
        for i in range(len(t)):
            t_letters[t[i]] = t_letters.get(t[i], 0) + 1
        
        print s_letters, t_letters
        return s_letters == t_letters