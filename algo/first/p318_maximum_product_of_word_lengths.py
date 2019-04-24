class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_len = {}

        max_product = 0

        ord_a = ord('a')

        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord_a)

            max_len[mask] = max(max_len.get(mask, 0), len(word))

            for key, val in max_len.items():
                if not (mask & key):
                    max_product = max(max_product, len(word) * val)

        return max_product
