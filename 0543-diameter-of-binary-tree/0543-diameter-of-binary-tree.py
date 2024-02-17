class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        def get_depth(node):
            if not node:
                return 0

            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            self.max_length = max(self.max_length, left_depth+right_depth)

            return 1 + max(left_depth, right_depth)

        get_depth(root)

        return self.max_length