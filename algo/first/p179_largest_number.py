class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a = [str(n) for n in nums]
        a.sort(cmp=lambda x, y: cmp(y + x, x + y))
        return ''.join(a).lstrip('0') or '0'
