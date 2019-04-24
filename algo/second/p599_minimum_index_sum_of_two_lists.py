class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {v: i for i, v in enumerate(list1)}

        least = 1e9
        res = []

        for i, val in enumerate(list2):
            tmp = d.get(val, 1e9)
            if i + tmp < least:
                least = i + tmp
                res = [val]
            elif i + tmp == least:
                res.append(val)

        return res
