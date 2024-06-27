class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def balanceBST(self, root):
        self.arr: list[int] = []

        def traversal(root: TreeNode):
            if root:
                traversal(root.left)
                self.arr.append(root.val)
                traversal(root.right)

        traversal(root)
        return makeTree(self.arr, 0, len(self.arr) - 1)


def makeTree(arr, lo, hi):
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    left = makeTree(arr, lo, mid - 1)
    right = makeTree(arr, mid + 1, hi)
    return TreeNode(arr[mid], left, right)


root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
root = root.balanceBST(root)
