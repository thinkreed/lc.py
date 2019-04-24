from collections import Counter
from collections import defaultdict


class FreqStack(object):

    def __init__(self):
        self.freq_counter = Counter()
        self.d = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        freq = self.freq_counter
        d = self.d
        freq[x] += 1
        self.max_freq = max(self.max_freq, freq[x])
        d[freq[x]].append(x)

    def pop(self):
        """
        :rtype: int
        """
        freq = self.freq_counter
        d = self.d
        max_freq = self.max_freq
        x = d[max_freq].pop()
        if not d[max_freq]:
            self.max_freq = max_freq - 1

        freq[x] -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
