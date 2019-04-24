from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True

            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in email_map[email]:
                    dfs(neighbor, emails)

        visited = [False] * len(accounts)
        email_map = defaultdict(list)
        res = []

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email_map[account[j]].append(i)

        for i, account in enumerate(accounts):
            if visited[i]:
                continue

            name = account[0]
            emails = set()

            dfs(i, emails)

            res.append([name] + sorted(emails))

        return res
