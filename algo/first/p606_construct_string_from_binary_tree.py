class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''

        left_result = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right_result = '({})'.format(self.tree2str(t.right)) if t.right else ''

        return '{}{}{}'.format(t.val, left_result, right_result)
