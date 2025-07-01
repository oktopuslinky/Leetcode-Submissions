class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        # if letter repeated then += 1
        # 

        output = len(word)
        for i, letter in enumerate(word[1:]):
            if letter != word[i]:
                output -= 1
        return output