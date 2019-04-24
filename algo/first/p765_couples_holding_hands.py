class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        pos = [0] * n

        def swap(x, y):
            temp = row[x]
            pos[temp] = y
            pos[row[y]] = x
            row[x] = row[y]
            row[y] = temp

        for i in range(n):
            pos[row[i]] = i

        count = 0

        for i in range(0, n, 2):
            j = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
            if row[i + 1] != j:
                swap(i + 1, pos[j])
                count += 1

        return count
