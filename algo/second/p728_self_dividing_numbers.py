class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        is_ok = lambda num: '0' not in str(num) and all(num % int(d) == 0 for d in str(num))
        return filter(is_ok, range(left, right + 1))
