class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        root = set(dict)

        def map_word_to_root(word):
            for i in range(1, len(word)):
                if word[:i] in root:
                    return word[:i]
            return word

        return " ".join(map(map_word_to_root, sentence.split()))
