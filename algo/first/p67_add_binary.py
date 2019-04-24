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
        result = ''

        while i >= 0 or j >= 0:
            sumary = carry
            if i >= 0:
                sumary += ord(a[i]) - ord_0
                i -= 1

            if j >= 0:
                sumary += ord(b[j]) - ord_0
                j -= 1

            result += str(sumary % 2)
            carry = sumary // 2

        if carry > 0:
            result += str(carry)

        return result[::-1]
