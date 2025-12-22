class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        word_len = len(strs[0])
        columns = [[] for _ in range(word_len)]
        for string in strs:
            for col in range(len(string)):
                columns[col] += string[col]
        
        to_delete = 0

        for col in columns:
            if col != sorted(col):
                print col, sorted(col)
                to_delete += 1
        
        return to_delete