
class TreeNode:					# 二叉树节点的定义
    def __init__(self, x):
        self.val = x		# 节点值
        self.left = None	# 左侧子节点
        self.right = None 	# 右侧子节点
        
    def rob(self, root):
        a = self.helper(root)		#a是一个二维数组，为root的[偷值，不偷值]
        return max(a[0],a[1])		#返回两个值的最大值，此值为小偷最终获得的财富值。
    def helper(self,root):	#参数为root节点，helper方法输出一个二维数组：root节点的[偷值，不偷值]
        if(root==None):		#如果root节点为空，输出[0,0]
            return [0,0]
        left = self.helper(root.left)		#left是一个二维数组，为root左侧子节点的[偷值，不偷值]
        right = self.helper(root.right)	#right也是一个二维数组，为root右侧子节点的[偷值，不偷值]
        robValue = root.val + left[1]+ right[1]				#root的偷值
        skipValue = max(left[0],left[1]) + max(right[0],right[1])		#root的不偷值
        return [robValue, skipValue]					#输出小偷可获得的最大金额

node1= TreeNode(3)
node2= TreeNode(4)
node3= TreeNode(5)
node4= TreeNode(1)
node5= TreeNode(3)
node6= TreeNode(1)
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.right=node6

robToolObject=TreeNode(0)
print(robToolObject.rob(root=node1))
