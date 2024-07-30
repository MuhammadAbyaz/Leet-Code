class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMode(root: TreeNode) -> list[int]:
    if root.right is None and root.left is None:
        return [root.val]
    freq: dict[int, int] = {}
    def traverse(root):
        if not root:
            return
        traverse(root.left)
        freq[root.val] = freq.get(root.val,0) + 1
        traverse(root.right)
    traverse(root)
    return [key for key in freq.keys() if freq[key] == max(freq.values())]

root = TreeNode(1,None,TreeNode(1,TreeNode(2)))
print(findMode(root))