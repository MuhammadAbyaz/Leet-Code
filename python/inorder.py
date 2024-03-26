class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root, values):
    if root is None:
        return
    traverse(root.left, values)
    values.append(root.val)
    traverse(root.right, values)


def inorderTraversal(root: TreeNode) -> list[int]:
    values: list[int] = []
    traverse(root, values)
    return values
