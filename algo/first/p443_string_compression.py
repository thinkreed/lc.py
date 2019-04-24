class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        start = 0
        current_char_count = 0
        for i, c in enumerate(chars):
            current_char_count += 1
            if i == len(chars) - 1 or c != chars[i + 1]:
                chars[start] = c
                start += 1
                if current_char_count > 1:
                    length_string = str(current_char_count)
                    for char in length_string:
                        chars[start] = char
                        start += 1

                current_char_count = 0

        return start
