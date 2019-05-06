class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        m = len(num1)
        n = len(num2)

        pos = [0 for _ in range(m + n)]
        res = []

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1

                s = mul + pos[p2]

                pos[p1] += s // 10
                pos[p2] = s % 10

        for num in pos:
            if len(res) == 0 and num == 0:
                continue

            res.append(num)

        return ''.join(str(e) for e in res) if len(res) != 0 else '0'
