class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        ord_0 = ord('0')

        res = ''

        while i >= 0 or j >= 0:
            tmp = carry

            if i >= 0:
                tmp += ord(a[i]) - ord_0
                i -= 1

            if j >= 0:
                tmp += ord(b[j]) - ord_0
                j -= 1

            res += str(tmp % 2)

            carry = tmp // 2

        if carry > 0:
            res += str(carry)

        return res[::-1]
