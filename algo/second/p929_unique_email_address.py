class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = set();
        for email in emails:
            local, domain = email.split("@")
            local = "".join(local.split('+')[0].split('.'))
            email = local + '@' + domain
            s.add(email)

        return len(s)
