class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        word_len = len(strs[0])
        cols_to_consider = [_ for _ in range(word_len)]
        
        for i in range(1, len(strs)):
            for col in cols_to_consider:
                if strs[i][col] < strs[i-1][col]:
                    cols_to_consider.remove(col)
        
        return word_len - len(cols_to_consider)