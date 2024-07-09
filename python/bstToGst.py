class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode, total):
    if root is None:
        return
    dfs(root.right, total)
    total.append(root.val)
    root.val = sum(total)
    dfs(root.left, total)


def bstToGst(root: TreeNode) -> TreeNode:
    total: list[int] = []
    dfs(root, total)
    return root


root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
root = bstToGst(root)
