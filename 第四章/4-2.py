import sys
class Solution:
    def maxPathSum(self, root):				#输出最大路径和的方法
        return max(self.helper(root))		#调用helper方法，传入根节点，输出返回的两个值的最大值
    def helper(self, root):				#helper方法，输出一个二维数组 [ 不停值，停值 ]
        if root==None:				#如果节点为空，输出两个最小值
            return -sys.float_info.max, -sys.float_info.max
        leftY,leftN = self.helper(root.left)			#得到左子节点的不停值与停值
        rightY,rightN = self.helper(root.right)		#得到右子节点的不停值与停值
        yes = max(root.val+leftY,root.val+rightY,root.val)			#不停值
        no = max(leftN,rightN,leftY,rightY,root.val+leftY+rightY) 		#停值
        return yes,no					#输出 [ 不停值，停值 ]

class TreeNode:  # 二叉树节点的定义
    def __init__(self, x):
        self.val = x  # 节点值
        self.left = None  # 左侧子节点
        self.right = None  # 右侧子节点

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(-2)
node4 = TreeNode(10)
node5 = TreeNode(12)
node6 = TreeNode(2)
node7 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

sol = Solution()
print(sol.maxPathSum(root=node1))

