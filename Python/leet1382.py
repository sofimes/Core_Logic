# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: In-order traversal to collect nodes (not values)
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Build balanced BST using the nodes themselves
        def buildBST(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = nodes[mid]
            node.left = buildBST(l, mid - 1)
            node.right = buildBST(mid + 1, r)
            return node
        
        return buildBST(0, len(nodes) - 1)
