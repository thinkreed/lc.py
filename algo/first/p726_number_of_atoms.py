from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula):
        d = defaultdict(int)
        count_of_eff = 1
        s = []
        em = ""
        count = 0
        i = 0
        for c in formula[::-1]:
            if c.isdigit():
                count += int(c) * (10 ** i)
                i += 1
            elif c == ")":
                s.append(count)
                count_of_eff *= count
                i = count = 0
            elif c == "(":
                count_of_eff //= s.pop()
                i = count = 0
            elif c.isupper():
                em += c
                d[em[::-1]] += (count or 1) * count_of_eff
                em = ""
                i = count = 0
            elif c.islower():
                em += c
        return "".join(k + str(v > 1 and v or "") for k, v in sorted(d.items()))
