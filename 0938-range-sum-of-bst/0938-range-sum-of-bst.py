class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque([root])
        answer = []
        while queue:
            current = queue.popleft()
            if current.val >= low and current.val <= high:
                answer.append(current.val)
            
            if current.left :
                queue.append(current.left)
                
            if current.right:
                queue.append(current.right)
                
        return sum(answer)