class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        groups = {}
        output_groups = []

        for string in strs:
            string_hash = {}
            for letter in string:
                string_hash[letter] = string_hash.get(letter, 0) + 1
            
            found = False

            for group in groups.items():
                if group[1] == string_hash:
                    found = True
                    output_groups[group[0]].append(string)
            
            if not found:
                groups[len(groups)] = string_hash
                output_groups.append([string])

        return output_groups