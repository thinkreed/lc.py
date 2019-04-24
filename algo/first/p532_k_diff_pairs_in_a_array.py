class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        result_set = set()
        candidate_set = set()
        for num in nums:
            if num - k in candidate_set:
                result_set.add(num - k)
            if num + k in candidate_set:
                result_set.add(num)
            candidate_set.add(num)

        return len(result_set)
