#爬楼梯，一次可爬一阶或两阶
def upstairs(n):
	"""
	利用递归实现动态规划算法过程
	:param n:阶梯级数
	:return: 计算结果

	"""
	a = 1  # 初始化边界值
	b = 2
	temp = 0
	if  n < 1:				#判断当前台阶级数小于1
		print(0)
		return
	if  n == 1:				#判断当前台阶级数为1
		print(1)
		return

	if  n == 2:				#判断当前台阶级数为2
		print(2)
		return

	for i in range(3,n+1):		#迭代求解各级台阶的走法数量
		# print(i)
		temp = a + b
		a = b
		b = temp
	return temp			#返回计算结果
	
	
print(upstairs(5))