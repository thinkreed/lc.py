class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in sorted(strs):
            key = tuple(sorted(s))
            d[key] = d.get(key, []) + [s]

        return list(d.values())
