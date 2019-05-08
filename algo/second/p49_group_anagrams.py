class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cache = {}

        for s in strs:
            ordered = ''.join(sorted(s))

            if ordered in cache:
                cache[ordered] += [s]
            else:
                cache[ordered] = [s]
        return list(cache.values())
