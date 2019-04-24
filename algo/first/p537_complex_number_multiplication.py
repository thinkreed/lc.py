class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        (a+bi)(c+di) = (ac - bd) + (ad+bc)i.
        :type a: str
        :type b: str
        :rtype: str
        """
        x, y = map(int, a[:-1].split('+'))
        z, i = map(int, b[:-1].split('+'))
        return '%d+%di' % (x * z - y * i, x * i + y * z)
