class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        groups = {}

        for string in strs:
            string_group = "".join(sorted(string))
            if string_group not in groups:
                groups[string_group] = []
            groups[string_group].append(string)

        return groups.values()