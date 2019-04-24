from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def create_struct(root):
            if not root:
                return "invalid"

            struct = "%s,%s,%s" % (str(root.val), create_struct(root.left), create_struct(root.right))
            nodes[struct].append(root)
            return struct

        nodes = defaultdict(list)
        create_struct(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]
