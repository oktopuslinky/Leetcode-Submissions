class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        # if letter repeated then += 1
        # 

        output = len(word)
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                output -= 1
        return output