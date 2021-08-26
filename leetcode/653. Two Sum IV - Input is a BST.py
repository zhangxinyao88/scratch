# way 1 - DFS tree -> Hash Set
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        theset = set()

        def check_set(root):
            if not root:
                return False
            if k - root.val in theset:
                return True
            theset.add(root.val)
            return check_set(root.left) or check_set(root.right)

        return check_set(root)


# way 2 - tree -> sorted list and two sum
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def make_list(root):
            if root is None:
                return []
            return make_list(root.left) + [root.val] + make_list(root.right)
        
        lst = make_list(root)
        i, j = 0, len(lst) - 1

        while i < j:
            if lst[i] + lst[j] == k:
                return True
            if lst[i] + lst[j] < k:
                i += 1
            else:
                j -= 1

        return False
