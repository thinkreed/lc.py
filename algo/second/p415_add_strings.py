class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)

        res = []
        carry = 0
        ord_0 = ord('0')

        while len(num2) > 0 or len(num1) > 0:
            x = ord(num1.pop()) - ord_0 if len(num1) > 0 else 0
            y = ord(num2.pop()) - ord_0 if len(num2) > 0 else 0

            s = x + y + carry
            res.append(s % 10)
            carry = s // 10

        if carry:
            res.append(carry)

        return ''.join([str(i) for i in res[::-1]])
