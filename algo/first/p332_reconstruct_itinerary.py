from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        def visit(port):
            while dests[port]:
                visit(dests[port].pop())
            res.append(port)

        dests = defaultdict(list)
        for fr, to in sorted(tickets)[::-1]:
            dests[fr] += to,

        res = []

        visit('JFK')
        return res[::-1]
