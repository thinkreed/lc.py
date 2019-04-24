class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []

        for num in nums1:
            d[num] = d.get(num, 0) + 1

        for num in nums2:
            if num in d and d[num] > 0:
                res.append(num)
                d[num] -= 1

        return res
